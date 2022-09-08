set PATH=c:\python39\;c:\python39\scripts\;%PATH%
set FILE_FILTER=%1
set TESTS_FILTER="%2"
set MODE=%3
set RETRIES=%4
set UPDATE_REFS=%5

if not defined RETRIES set RETRIES=2
if not defined UPDATE_REFS set UPDATE_REFS="No"

python prepare_test_cases.py --mode_name %MODE%

python -m pip install -r ..\jobs_launcher\install\requirements.txt
python ..\jobs_launcher\executeTests.py --test_filter %TESTS_FILTER% --file_filter %FILE_FILTER% --tests_root ..\jobs --work_root ..\Work\Results --work_dir WebViewer --cmd_variables Tool "C:\Program Files\AMD\AMD RenderStudio\AMD RenderStudio.exe" ResPath "C:\TestResources\web_viewer_autotests_assets" mode %MODE% retries %RETRIES% UpdateRefs %UPDATE_REFS%