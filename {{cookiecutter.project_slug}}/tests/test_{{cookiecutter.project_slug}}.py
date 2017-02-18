import unittest

class Test{{cookiecutter.project_camelcase}}(unittest.TestCase):
    maxDiff = None
    
    # @unittest.skipIf(os.environ.get('FAST'), "Only running fast tests.") # Uncomment for a slow test
    def test_something(self):
        input = {
            'key': 'value'
        }
        output = {{cookiecutter.project_slug}}.run(input, { })
        self.assertEqual(output, { 'key': 'value' })

