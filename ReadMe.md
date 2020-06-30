
allure report sencitivity apply
# @allure.severity(allure.severity_level.MINOR)
# @allure.severity(allure.severity_level.NORMAL)
# @allure.severity(allure.severity_level.CRITICAL)

for run testcase with allure
pytest -v -s --alluredir="D:\pythonWorkspace\PyTestProjectTemplate\reports" -m smoke

for genrate allure report
allure serve D:\pythonWorkspace\PyTestProjectTemplate\reports

for run HTML report
pytest --html = report.html



for marker
pytest -m smoke
pytest -m "smoke and regration"
pytest -m "smoke or regration"
pytest -m "not regration"


for command line print
pytest -v --capture=no
