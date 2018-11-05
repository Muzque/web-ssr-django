def make_key(key, key_prefix, version):
    return ':'.join([key_prefix, str(version), key])
