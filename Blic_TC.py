from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

def load_blic(url):
    driver=webdriver.Chrome(service=Service('C:\Windows\chromedriver.exe'))
    driver.maximize_window()
    driver.get(url)
    return driver

def zatvori_reklamu(driver):
    sleep(1)
    reklama = driver.find_elements(By.ID, 'close_adhesion')
    if reklama:
        reklama[0].click()
        print("Reklama zatvorena.")
    else:
        print("Nema reklame.")

def test_registrovanja():
    driver=load_blic("https://www.blic.rs/")
    sleep(1)
    zatvori_reklamu(driver)
    driver.find_element(By.ID,'login-button').click()
    sleep(1)
    driver.find_element(By.ID,'first-step-register').click()
    sleep(1)
    driver.find_element(By.NAME,'email').send_keys('rsasa84@yahoo.com')
    driver.find_element(By.NAME,'password').send_keys('Sdebo84!')
    driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div/div/form/div[7]/div[1]/label/div[1]").click()
    sleep(1)
    driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div/div/form/div[7]/div[2]/label/div[1]/div").click()
    sleep(2)
    reg = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div")
    reg.screenshot('Blic slike/Registrovanje email.png')
    driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div/div/form/div[8]/button/div/div").click()
    sleep(2)
    driver.quit()

def test_logovanje_sa_pogresnom_sifrom():
    driver=load_blic('https://www.blic.rs/')
    sleep(1)
    zatvori_reklamu(driver)
    driver.find_element(By.ID, 'login-button').click()
    sleep(1)
    driver.find_element(By.NAME,'email').send_keys('rsasa84@yahoo.com')
    sleep(1)
    driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[1]/div[4]/form/div[2]/button/div/div").click()
    sleep(1)
    driver.find_element(By.NAME, 'password').send_keys('SD')
    sleep(2)
    driver.find_element(By.ID, 'native-login-btn').click()
    sleep(2)
    try:
        poruka=driver.find_element(By.ID, 'native-login-btn')
        print('Neuspesno logovanje', poruka.text)
    except NoSuchElementException:
        print('Uspesno smo se ulogovali')
    driver.quit()

def test_registrovanja_sa_praznim_poljima():
    driver = load_blic("https://www.blic.rs/")
    sleep(1)
    zatvori_reklamu(driver)
    driver.find_element(By.ID, 'login-button').click()
    sleep(1)
    driver.find_element(By.ID, 'first-step-register').click()
    sleep(1)
    driver.find_element(By.NAME, 'email').send_keys('')
    driver.find_element(By.NAME, 'password').send_keys('')
    driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div/form/div[8]/button/div/div").click()
    sleep(2)
    reg = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div")
    reg.screenshot('Blic slike/Prazna polja pri registrovanju.png')
    driver.quit()

def test_login_sa_pozitivnim_ishodom():
    driver = load_blic('https://www.blic.rs/')
    sleep(1)
    zatvori_reklamu(driver)
    driver.find_element(By.ID, 'login-button').click()
    sleep(1)
    driver.find_element(By.NAME, 'email').send_keys('rsasa84@yahoo.com')
    sleep(1)
    driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[1]/div[4]/form/div[2]/button/div/div").click()
    sleep(1)
    driver.find_element(By.NAME, 'password').send_keys('Sdebo84!')
    sleep(1)
    driver.find_element(By.ID, 'native-login-btn').click()
    sleep(2)
    try:
        uspesno = driver.find_element(By.XPATH, "/html/body/header/div[2]/div[1]/nav/ul/li[1]").text
        if 'Naslovna' in uspesno:
            print('Uspesno smo se ulogovali.')
            assert True
        else:
            print('Nismo uspeli da se ulogujemo.')
            assert False
    except NoSuchElementException:
        try:
            greska = driver.find_element(By.ID, 'native-login-error-message').text
            print('Greska pri logovanju:', greska)
            assert False
        except NoSuchElementException:
            print('Nismo ispravno upisali sifru')
            assert False
    driver.quit()

def test_dugme_za_sakrivanje_sifre():
    driver = load_blic('https://www.blic.rs/')
    sleep(1)
    zatvori_reklamu(driver)
    driver.find_element(By.ID, 'login-button').click()
    sleep(1)
    driver.find_element(By.ID, 'first-step-register').click()
    sleep(1)
    driver.find_element(By.NAME, 'password').send_keys('SD')
    sleep(2)
    prikazi=driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div/div/form/div[5]/div/div[1]/div")
    for _ in range(2):
        prikazi.click()
        sleep(1)
        print('Nije u finkciji polje za citanje sifri')
    lozinka = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div")
    lozinka.screenshot('Blic slike/Nije skrivena sifra.png')
    driver.quit()

def test_manje_od_8_karaktera():
    driver = load_blic('https://www.blic.rs/')
    sleep(1)
    zatvori_reklamu(driver)
    driver.find_element(By.ID, 'login-button').click()
    sleep(1)
    driver.find_element(By.ID, 'first-step-register').click()
    sleep(1)
    driver.find_element(By.NAME, 'password').send_keys('sdeboo')
    sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div/form/div[5]/div/div[1]/div").click()
    sleep(1)
    karakter = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div")
    karakter.screenshot('Blic slike/Poruka sa 6 karaktera.png')
    driver.quit()

def test_zaboravili_lozinku():
    driver = load_blic('https://www.blic.rs/')
    sleep(1)
    zatvori_reklamu(driver)
    driver.find_element(By.ID, 'login-button').click()
    sleep(1)
    driver.find_element(By.NAME, 'email').send_keys('rsasa84@yahoo.com')
    sleep(1)
    driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[1]/div[4]/form/div[2]/button/div/div").click()
    sleep(1)
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Zaboravili ste lozinku?').click()
    sleep(2)
    zaboravljena_lozinka=driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div")
    zaboravljena_lozinka.screenshot('Blic slike/Lozinka poslata na email.png')
    driver.quit()

def test_naslovi_na_baru_blica():
    driver = load_blic('https://www.blic.rs/')
    sleep(1)
    zatvori_reklamu(driver)
    driver.find_element(By.XPATH, "/html/body/header/div[2]/div[1]/nav/ul/li[1]/a").click()
    sleep(1)

    naslovi = driver.find_elements(By.XPATH, "/html/body/header/div[3]/div/nav/ul/li/a")
    niz_naslova=len(naslovi)
    print(f"Pronadjeno {niz_naslova} naslova.")
    for i in range(len(naslovi)):
        try:
            naslovi = driver.find_elements(By.XPATH, "/html/body/header/div[3]/div/nav/ul/li/a")
            naslov = naslovi[i]
            print(f"Naslov {i+1}: {naslov.text}")
            naslov.click()
            sleep(1)
            zatvori_reklamu(driver)
            print("Otvorena stranica:", driver.current_url)
            driver.back()
            sleep(1)
            zatvori_reklamu(driver)
        except Exception as greska:
            print(f"Greska kod naslova {i+1}: {greska}")
    driver.quit()

def test_otvaranja_naslova_unutar_naslova():
    driver=load_blic('https://www.blic.rs/')
    sleep(1)
    zatvori_reklamu(driver)
    driver.find_element(By.XPATH, "/html/body/header/div[2]/div[1]/nav/ul/li[1]/a").click()
    sleep(1)

    odabrane_stranice = (0, 1, 5, 8)
    for i in odabrane_stranice:
        naslovi = driver.find_elements(By.XPATH, "/html/body/header/div[3]/div/nav/ul/li/a")
        if i < len(naslovi):
            naslov = naslovi[i]
            print(f'Naslov {i + 1}: {naslov.text}')
            try:
                naslov.click()
                zatvori_reklamu(driver)
                if i == max(odabrane_stranice):
                    try:
                        unutrasnji_naslov = driver.find_element(By.XPATH,"/html/body/main/div/section/div/div[2]/section[2]/article[1]")
                        print('Unutrasnji naslov:', unutrasnji_naslov.text)
                        unutrasnji_naslov.click()
                        print("Na unutrasnjoj stranici:", driver.current_url)
                        driver.back()
                        sleep(1)
                        slika = driver.find_element(By.XPATH,"/html/body/main/div/section/div/div[2]/section[2]/article[1]/div[1]")
                        slika.screenshot('Blic slike/Slika sa sajta kulture.png')
                        sleep(1)
                    except Exception as error:
                        print('Greska pri kliku na unutrasnji naslov:', error)
                driver.back()
                sleep(1)
                print('Na stranici:', driver.current_url)
            except Exception as error:
                print('Greska:', error)
        else:
            print(f'Odabrani naslov {i} ne postoji.')
    driver.quit()

def test_kursna_lista():
    driver=load_blic('https://www.blic.rs/')
    zatvori_reklamu(driver)

    driver.find_element(By.XPATH,"/html/body/header/div[1]/div/div[2]/span[2]/a").click()
    driver.find_element(By.XPATH,"/html/body/main/div/section/div[1]/select[1]").click()
    driver.find_element(By.ID,'from-USD').click()
    print('Kliknut kurs')
    sleep(2)
    driver.find_element(By.XPATH,"/html/body/main/div/section/div[1]/select[2]").click()
    driver.find_element(By.ID,'to-GBP').click()
    print('Kliknut drugi kurs')
    driver.find_element(By.ID, 'amount').clear()
    driver.find_element(By.ID,'amount').send_keys('500')
    sleep(1)
    rezultat=driver.find_element(By.ID,'currencyCalculatorResult').text
    print(f'Dobijeni rezultat je: {rezultat}')
    driver.quit()

def test_vremenska_prognoza():
    driver=load_blic('https://www.blic.rs/')
    zatvori_reklamu(driver)

    driver.find_element(By.ID,'weatherCarousel').click()
    sleep(1)
    driver.find_element(By.ID,'search-box').send_keys('Srem')
    sleep(1)
    grad=driver.find_element(By.XPATH, "/html/body/main/section/div[1]/div[1]/div/div/div[1]/a")
    mesto=grad.text
    grad.click()
    print(f'Odabrano mesto je: {mesto}')
    vreme=driver.find_element(By.XPATH,"/html/body/main/section/div[1]/div[2]")
    vreme.screenshot('Blic slike/Vreme.png')
    sleep(1)
    driver.quit()

def test_obliznja_mesta():
    driver = load_blic('https://www.blic.rs/')
    zatvori_reklamu(driver)

    driver.find_element(By.ID, 'weatherCarousel').click()
    sleep(1)
    driver.find_element(By.ID, 'search-box').send_keys('Pirot')
    sleep(1)
    zatvori_reklamu(driver)

    grad = driver.find_element(By.XPATH, "/html/body/main/section/div[1]/div[1]/div/div/div[1]/a")
    mesto=grad.text
    grad.click()
    print(f'Odabrano mesto je: {mesto}')
    sleep(2)
    zatvori_reklamu(driver)
    reklama=driver.find_element(By.XPATH,"/html/body/main/section/div[1]/div[3]")
    driver.execute_script("arguments[0].scrollIntoView();",reklama)
    sleep(2)

    indeks=(2,5,9)
    for i in indeks:
        gradovi=driver.find_elements(By.XPATH, "/html/body/main/section/div[3]/ul/li/a")
        if i < len(gradovi):
            mesto=gradovi[i]
            naziv=mesto.text
            print(f'Na mesto {i+1} je: {naziv}')
            mesto.click()
            sleep(2)
            panel_za_vreme=driver.find_element(By.XPATH,"/html/body/main/section/div[1]/div[2]")
            imena= naziv
            panel_za_vreme.screenshot(f'Blic slike/{imena}.png')
            print(f'Prognoza za: {naziv}')
            driver.back()
        else:
            print(f'Odabrani {i} ne postoji')
    driver.quit()

def test_ringier_sebia():
    driver=load_blic('https://www.blic.rs/')
    zatvori_reklamu(driver)

    vreme_za_skrolovanje= 0.10
    skrolovanje = 2000
    zatvori_reklamu(driver)
    poslednja_pozicija = driver.execute_script("return document.body.scrollHeight")
    trenutna_pozicija = 0
    while trenutna_pozicija < poslednja_pozicija:
        driver.execute_script(f"window.scrollBy(0, {skrolovanje});")
        trenutna_pozicija += skrolovanje
        sleep(vreme_za_skrolovanje)
        poslednja_pozicija = driver.execute_script("return document.body.scrollHeight")
    zatvori_reklamu(driver)

    pozicija = 0
    while True:
        ringier_sebia = driver.find_elements(By.XPATH, "/html/body/footer/div/div[2]/div[1]/div[2]/ul//a")
        if pozicija >= len(ringier_sebia):
            break

        sajt = ringier_sebia[pozicija]
        print(f'Kliknuo na naslov: {sajt.text}')
        original = driver.current_window_handle
        sajt.click()
        sleep(1)

        for handle in driver.window_handles:
            if handle != original:
                driver.switch_to.window(handle)
                break

        print(f'Trenutni URL: {driver.current_url}')
        sleep(1)

        driver.close()
        driver.switch_to.window(original)
        sleep(1)
        pozicija += 1
    print("Zavrsen pregled sajtova!")
    driver.quit()

def test_najnovihih_vesti():
    driver = load_blic('https://www.blic.rs/')
    zatvori_reklamu(driver)

    vreme_za_skrolovanje = 0.1
    skrolovanje = 2000
    poslednja_pozicija = driver.execute_script("return document.body.scrollHeight")
    trenutna_pozicija = 0
    while trenutna_pozicija < poslednja_pozicija:
        driver.execute_script(f"window.scrollBy(0, {skrolovanje});")
        trenutna_pozicija += skrolovanje
        sleep(vreme_za_skrolovanje)
        poslednja_pozicija = driver.execute_script("return document.body.scrollHeight")

    vesti=driver.find_element(By.XPATH,"//a[contains(text(),'Najnovije vesti')]")
    driver.execute_script("arguments[0].click();",vesti)
    zatvori_reklamu(driver)
    sleep(2)
    driver.find_element(By.XPATH,"/html/body/main/div/section/div/section[1]/div[1]/article[1]/div[2]").click()
    zatvori_reklamu(driver)
    naslov=driver.find_element(By.XPATH,"/html/body/main/div[2]/section/div")
    driver.execute_script("arguments[0].scrollIntoView();",naslov)
    zatvori_reklamu(driver)
    sleep(2)
    driver.quit()

def test_video_snimak():
    driver = load_blic('https://www.blic.rs/')
    zatvori_reklamu(driver)
    driver.find_element(By.XPATH,"/html/body/header/div[2]/div[1]/nav/ul/li[4]").click()
    sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/nav/div[2]/div[4]/div[1]/div[1]/div[6]/a").click()
    sleep(1)
    zatvori_reklamu(driver)
    driver.find_element(By.XPATH,"/html/body/div[1]/main/div[3]/div[1]/div[2]/div/div[2]/div/ul/li[2]/div/a/div/picture/img").click()
    sleep(2)
    driver.quit()