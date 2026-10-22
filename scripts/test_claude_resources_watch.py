"""Offline regression checks for the Claude Resources weekly intake."""
import unittest
from datetime import date
from claude_resources_watch import canonical, domain_for, parse, publisher_dates, relevant


class SourceWatchTests(unittest.TestCase):
    def test_joined_article_date_and_relative_link(self):
        html = ('<a href="/resources/articles/agent-observability-on-the-claude-platform">'
                '<span>Article</span><span>Oct 14, 2026</span>'
                '<span>Agent observability on the Claude Platform</span></a>')
        got = publisher_dates(parse(html), "https://claude.com/resources/articles")
        self.assertEqual(got[
            "https://claude.com/resources/articles/agent-observability-on-the-claude-platform"][0],
            date(2026, 10, 14))

    def test_date_when_adjacent_to_article_label(self):
        html = ('<a href="https://claude.dev/blog/solving-code-review-at-anthropic/">'
                'ArticleOct 16, 2026 How the Claude Code team does code review</a>')
        got = publisher_dates(parse(html), "https://claude.com/resources")
        self.assertEqual(len(got), 1)
        self.assertEqual(next(iter(got.values()))[0], date(2026, 10, 16))

    def test_no_article_card_is_not_a_new_item(self):
        html = '<a href="/resources/articles">Articles</a>'
        self.assertEqual(publisher_dates(parse(html), "https://claude.com/resources"), {})

    def test_first_party_host_and_query_normalization(self):
        self.assertEqual(
            canonical("https://claude.dev/blog/example/?ref=resource"),
            "https://claude.dev/blog/example")
        self.assertEqual(canonical("https://evil.example/steal"), "")

    def test_engineering_relevance_not_partner_press(self):
        self.assertTrue(relevant("Agent observability with OpenTelemetry"))
        self.assertFalse(relevant("HCLTech joins Claude Partner Network"))
        self.assertEqual(domain_for("AI Code Review for pull requests"), "verification")


if __name__ == "__main__":
    unittest.main()
