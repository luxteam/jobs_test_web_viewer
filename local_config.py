tool_name = 'render_studio'
report_type = 'default'
show_skipped_groups = True
tracked_metrics = {
    'render_time': {'displaying_name': 'Render time', 'function': 'sum', 'displaying_unit': 's'}
}
tracked_metrics_files_number = 10000
analyze_render_time = {"max_diff": 0.05}
show_execution_time = True
show_performance_tab = True
tracked_metrics_charts_location = 'performance'
show_time_taken = False
show_render_time = True
hide_zero_render_time = True
show_render_log = False
update_baselines_feature_supported = True
domain = '<domain_name>'