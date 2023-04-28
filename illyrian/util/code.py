__all__ = ['hash', 'L_RED', 'L_GREEN', 'L_EMPH', 'L_RESET']

import hashlib
import base64

#-------------------------------------------------------------------------------
def hash(content: bytes, algo: str = 'sha256', no_pad: bool = True) -> str:
	cls = getattr(hashlib, algo, None)
	if cls is None:
		return False
	m = cls()
	m.update(content)
	value = algo + '=' + base64.urlsafe_b64encode(m.digest()).decode("UTF-8")
	if no_pad:
		value = value.rstrip('=')
	return value

#-------------------------------------------------------------------------------
L_EMPH  = "\033[1m"
L_RED	= "\033[0;31m"
L_GREEN	= "\033[0;32m"
L_RESET = "\033[0m"

#-------------------------------------------------------------------------------