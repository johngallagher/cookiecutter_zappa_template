import {{cookiecutter.project_slug}}
import json
import merge

def run(event, context):
    return merge.dicts(event, {{cookiecutter.project_slug}}.run(event, context))

if __name__ == '__main__':
    event = {}
    context = {}
    result = run(event, context)
    print(json.dumps(result))
