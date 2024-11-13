import unittest

from CheckAndClean import CheckAndClean


class sanitizeTest(unittest.TestCase):
    cc = CheckAndClean("testing")

    def test_sanitize(self):
        TESTCASES = [
            [R"Bobby';Drop tables students;--",
             R"Bobby\'\;Drop tables students\;\-\-"],
            ["May I do that.", R"May I do that\."],
            ["", ""],
            [">; ls -al#", R"\>\; ls \-al\#"]
        ]

        self.assertEqual(self.cc.sanitize("'; SELECT * FROM Users; --"),
                         R"\'\; SELECT \* FROM Users\; \-\-")
        for case in TESTCASES:
            self.assertEqual(self.cc.sanitize(case[0]), case[1])

if __name__ == '__main__':
    unittest.main()
