import sys
import os
import unittest
from HTMLTestRunner import HTMLTestRunner
from Data.parameters import Data
from TS import click_on_cqube_login,click_on_blocks
from TS.click_on_cqube_login import CqubeLogin
from get_dir import pwd
p = pwd()
sys.path.append(p.get_system_path())


# pwd = Data()
# sys.path.append(pwd.get_system_path())

class MyTestSuite(unittest.TestCase):

    def test_Issue(self,month):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_cqube_login.CqubeLogin),
            # unittest.defaultTestLoader.loadTestsFromTestCase(click_on_blocks.SAR)

        ])
        #html_report_generate_path = Data()
        p = pwd()
        outfile = open(p.get_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream = outfile,
            title = month + 'Test Report',
            verbosity = 1,
            description = 'Smoke Tests'

        )

        runner1.run(smoke_test)
        outfile.close()


if __name__ == '__main__':
    unittest.main()
