# config
chromedriver_path = '/mnt/data/Workspace/webdrivers/chromedriver_89.0.4389.23'
ip_map_path = 'pollingsituajakali_ip_map.json'
target_url = 'https://pollingsituajakali.xyz/pollingxxxxxxxxxxx'
target = 'HARIYONO'
n_repeat = 1

if __name__ == '__main__':
    # get n_repeat if provided as argument
    if len(sys.argv) > 1:
        n_repeat = int(sys.argv[1])

    # load ip map if exists
    ip_map = {}
    if os.path.isfile(ip_map_path):
        with open(ip_map_path) as f:
            ip_map = json.load(f)

    # proxy generator
    proxy_gen = ProxyGenerator(Scrapper(category='ALL', print_err_trace=False))

    # repeat n_repeat times
    count = 0
    while count < n_repeat:
        print('Attempt #' + str(count+1))
        driver = None
        proxy = None
        try:
            # get proxy
            print('> Finding proxy..')
            while not proxy or proxy in ip_map:
                proxy = proxy_gen.generate()
                # time.sleep(1)
            print(f'> {proxy}')

            # setup selenium
            options = Options()
            options.add_argument('--headless')
            options.add_argument(f'--proxy-server={proxy}')
            driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
            driver.implicitly_wait(1)

            # click button
            driver.get(target_url)
            btn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, f'button[data-txt={target}]'))
            )
            btn.click()

            # wait for result
            # complete_element_id = 'chart'
            # complete_element_id = 'btnRefresh'
            complete_element_id = 'spanCount'
            print(f'> Waiting for {complete_element_id}..')
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, complete_element_id))
            )
            alerts = driver.find_elements_by_css_selector('.alert-danger')
            print(f'> alerts: {len(alerts)}')
            if len(alerts) <= 0:
                count += 1
                print('> Success')
            else:
                print('> Failed. IP has been used')

            # mark proxy
            ip_map[proxy] = 1
            with open(ip_map_path, 'w') as f:
                json.dump(ip_map, f)

        except Exception as e:
            print(f'> Failed. {e}')
        finally:
            if driver:
                driver.quit()

    print(f'Success: {count}')

##############################################################


if __name__ == '__main__':

    def get_num_repeat():
        num_repeat = 1
        if len(sys.argv) > 1:
            num_repeat = int(sys.argv[1])
        return num_repeat
    
    def generate_proxy(generator, ip_map):
        proxy = generator.generate()
        while proxy in ip_map:
            proxy = generator.generate()
        return proxy
    
    def update_count_on_alerts(alerts, count):        
        if len(alerts) <= 0:
            print('> Success')
            return count + 1
        print('> Failed. IP has been used')
        return count
    
      
    ip_map_path = 'pollingsituajakali_ip_map.json'
    with open(ip_map_path) as f:
        ip_map = json.load(f)

    proxy_gen = ProxyGenerator(Scrapper(category='ALL', print_err_trace=False))

    count = 0
    num_repeat = get_num_repeat()
    while count < num_repeat:

        print('Attempt #' + str(count+1))
        print('> Finding proxy..')
        proxy = generate_proxy(proxy_gen, ip_map)
        print(f'> {proxy}')

        options = Options()
        options.add_argument('--headless')
        options.add_argument(f'--proxy-server={proxy}')
        chromedriver_path = '/mnt/data/Workspace/webdrivers/chromedriver_89.0.4389.23'
        driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        driver.implicitly_wait(1)

        target_url = 'https://pollingsituajakali.xyz/pollingxxxxxxxxxxx'
        driver.get(target_url)
        target = 'HARIYONO'
        btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'button[data-txt={target}]'))
        )
        btn.click()

        complete_element_id = 'spanCount'
        print(f'> Waiting for {complete_element_id}..')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, complete_element_id))
        )
        alerts = driver.find_elements_by_css_selector('.alert-danger')
        print(f'> alerts: {len(alerts)}')

        count = update_count_on_alerts(alerts, count)
        ip_map[proxy] = 1
        with open(ip_map_path, 'w') as f:
            json.dump(ip_map, f)

        if driver:
            driver.quit()

    print(f'Success: {count}')
