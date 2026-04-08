import hmac
import hashlib
import base64

def generate_hmac_token(data: str, secret: str) -> str:
    """
    使用 HMAC-SHA256 生成令牌，并进行 Base64 URL 安全编码。
    """
    # 计算 HMAC-SHA256 摘要（原始字节）
    hmac_digest = hmac.new(
        secret.encode('utf-8'),
        data.encode('utf-8'),
        hashlib.sha256
    ).digest()

    # Base64 URL 编码并移除填充 '='
    return base64.urlsafe_b64encode(hmac_digest).rstrip(b'=').decode('utf-8')
