import json
import os
from typing import List, Optional

from lib.template_loader import ParamDef, ToolTemplate

_SEPARATOR = "================================"
_APIDOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "api-docs")


def load_apidocs_templates() -> List[ToolTemplate]:
    templates = []

    if not os.path.isdir(_APIDOCS_DIR):
        print("No api docs in path :{_APIDOCS_DIR}")
        return templates

    for group_dir in sorted(os.listdir(_APIDOCS_DIR)):
        group_path = os.path.join(_APIDOCS_DIR, group_dir)
        if not os.path.isdir(group_path):
            continue

        group_prefix = _load_group_prefix(group_path)

        for filename in sorted(os.listdir(group_path)):
            if not filename.endswith(".ms"):
                continue
            ms_path = os.path.join(group_path, filename)
            template = _parse_ms_file(ms_path, group_prefix)
            if template:
                templates.append(template)

    return templates


def _load_group_prefix(group_dir: str) -> str:
    group_json = os.path.join(group_dir, "group.json")
    if not os.path.exists(group_json):
        return ""
    with open(group_json, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("path", "").rstrip("/")


def _parse_ms_file(path: str, group_prefix: str) -> Optional[ToolTemplate]:
    with open(path, encoding="utf-8") as f:
        content = f.read()

    json_part = content.split(_SEPARATOR)[0].strip()
    try:
        data = json.loads(json_part)
    except json.JSONDecodeError:
        return None

    ms_path = data.get("path", "")
    if not ms_path:
        return None

    full_path = group_prefix + "/" + ms_path.lstrip("/")
    http_method = data.get("method", "POST").lower()
    name = data.get("name", ms_path)
    description = data.get("description") or name

    tool_name = _path_to_tool_name(full_path)
    params = []
    params.extend(_infer_params(data.get("parameters"), "query"))
    request_body = data.get("requestBodyDefinition") or {}
    params.extend(_infer_params(request_body.get("children") or [], "body"))
    response_config = _detect_response_config(data.get("responseBodyDefinition") or "{}")

    return ToolTemplate(
        name=tool_name,
        description=description,
        http_method=http_method,
        http_path=full_path,
        use_extract_data=True,
        path_params=[],
        constant_params={},
        params=params,
        empty_data_message="暂无数据",
        response_config=response_config,
    )


def _path_to_tool_name(path: str) -> str:
    parts = [p for p in path.strip("/").split("/") if p]
    return "get_" + "_".join(parts)

_TYPE_MAP = {
    "long": "int",
    "integer": "int",
    "int": "int",
    "double": "int",
    "float": "int",
    "number": "int",
    "string": "str",
    "integer": "int",
    "array": "list",
    "object": "dict",
}


def _infer_params(params_list: list, param_type: str) -> List[ParamDef]:
    params = []
    if not params_list:
        return params
    for item in params_list:
        data_type = _TYPE_MAP.get((item.get("dataType") or "").lower(), "str")

        params.append(ParamDef(
            name=item.get("name"),
            type=data_type,
            default=item.get("defaultValue"),
            required=item.get("required") or False,
            description=item.get("description") or "",
            body_key=item.get("name"),
            in_=param_type,
            conditional=True,
            community_map=False,
        ))
    return params


def _detect_response_config(response_body_str: str) -> dict:
    try:
        example = json.loads(response_body_str)
    except (json.JSONDecodeError, TypeError):
        return {"type": "scalar"}

    data = example.get("data", example)

    if isinstance(data, dict) and "list" in data:
        items = data.get("list", [])
        total_key = next((k for k in data if "total" in k.lower() and "page" not in k.lower()), "total_count")
        item_template = _make_item_template(items[0] if items else {})
        return {
            "type": "paginated_list",
            "list_key": "list",
            "total_key": total_key,
            "item_template": item_template,
        }

    if isinstance(data, list):
        item_template = _make_item_template(data[0] if data else {})
        return {"type": "list", "item_template": item_template}

    if isinstance(data, dict):
        fields = [{"label": k, "key": k} for k in data]
        return {"type": "scalar", "fields": fields}

    return {"type": "scalar"}


def _make_item_template(item: dict) -> str:
    if not isinstance(item, dict):
        return "  {index}. {item}"
    parts = [f"{k}={{{k}}}" for k in item]
    return "  {index}. " + ", ".join(parts)
