REPLACED = "the-text-has-been-replaced"

def setup(manifest, service_name, text_to_replace):
  manifest = manifest.replace(text_to_replace, REPLACED)
  return manifest

def teardown(manifest, service_name):
  manifest = manifest.replace(REPLACED, "not-any-more")
  return manifest
