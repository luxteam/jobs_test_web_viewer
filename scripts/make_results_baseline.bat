set PATH=c:\python39\;c:\python39\scripts\;%PATH%
set PYTHONPATH=..\jobs_launcher\;%PYTHONPATH%

set DELETE_BASELINES=%1
if not defined DELETE_BASELINES set DELETE_BASELINES=False

python -m pip install -r ..\jobs_launcher\install\requirements.txt
python ..\jobs_launcher\common\scripts\generate_baselines.py --results_root ..\Work\Results\RenderStudio --baseline_root ..\Work\GeneratedBaselines --remove_old %DELETE_BASELINES%