REPLACED = "the-text-has-been-replaced"

def create_flow(service_spec, deployment_spec, flow_uuid, text_to_replace):
    deployment_spec['template']['metadata']['labels']['app'] = deployment_spec['template']['metadata']['labels']['app'].replace(text_to_replace, REPLACED)
    deployment_spec['selector']['matchLabels']['app'] = deployment_spec['selector']['matchLabels']['app'].replace(text_to_replace, REPLACED)
    deployment_spec['template']['spec']['containers'][0]['name'] = deployment_spec['template']['spec']['containers'][0]['name'].replace(text_to_replace, REPLACED)
    
    config_map = {
        "original_text": text_to_replace
    }
    
    return {
        "deployment_spec": deployment_spec,
        "config_map": config_map
    }

def delete_flow(config_map, flow_uuid):
    print(config_map["original_text"])
