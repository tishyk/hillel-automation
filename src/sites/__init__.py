def get_site(test_dir):
    if test_dir.endswith('test_site1'):
        import site1_pages as site
    return site