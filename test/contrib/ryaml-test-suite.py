import json
from pathlib import Path

import ryaml

OUR_ROOT = Path(__file__).parent.resolve()


def run():
    passed = 0
    failed = 0
    test_dirs = [d for d in (OUR_ROOT / 'yaml-test-suite').iterdir() if d.is_dir()]
    for test_dir in test_dirs:
        infile = test_dir / 'in.yaml'
        jsonfile = test_dir / 'in.json'
        if infile.is_file() and jsonfile.is_file():
            print(f'Running {test_dir.name}')
            infile_text = infile.read_text(encoding='utf-8')
            jsonfile_text = jsonfile.read_text(encoding='utf-8')
            if not infile_text and not jsonfile_text:
                continue
            try:
                infile_obj = ryaml.loads(infile_text)
            except ryaml.InvalidYamlError:
                print('Failed to parse')
                failed += 1
                continue
            jsonfile_obj = json.loads(jsonfile_text)
            if infile_obj == jsonfile_obj:
                print('Passed')
                passed += 1
            else:
                print('Failed')
                failed += 1
                print('Expected:')
                print(json.dumps(jsonfile_obj, indent=2))
                print('Got:')
                print(json.dumps(infile_obj, indent=2))

    print(f'Passed: {passed}')
    print(f'Failed: {failed}')


if __name__ == '__main__':
    run()
