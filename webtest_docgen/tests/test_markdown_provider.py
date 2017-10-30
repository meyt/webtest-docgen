import unittest

from webtest_docgen import MarkdownProvider
from webtest_docgen.tests.helpers import WebAppProviderTestCase


class MarkdownProviderTestCase(WebAppProviderTestCase):

    def test_markdown_provider(self):
        from webtest_docgen.tests.helpers import mockup_app_tests
        mockup_app_tests(self.wsgi_app)

        provider = MarkdownProvider(
            docs_root=self.docs_root,
            destination_dir=self.get_destination_dir('markdown')
        )
        provider.generate()

if __name__ == '__main__':  # pragma: nocover
    unittest.main()