import os


class pwd():

    def get_driver_path(self):
        cwd = os.path.dirname(__file__)
        executable_path = os.path.join(cwd, 'Driver/chromedriver')
        return executable_path

    def get_system_path(self):
        pwd = os.path.dirname(__file__)
        return pwd

    def get_report_path(self):
        cwd = os.path.dirname(__file__)
        report_path = os.path.join(cwd, 'Reports/report.html')
        return report_path