import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk

clink = {
"China": "/world-population/china-population/",
"India": "/world-population/india-population/",
"United States": "/world-population/us-population/",
"Indonesia": "/world-population/indonesia-population/",
"Pakistan": "/world-population/pakistan-population/",
"Brazil": "/world-population/brazil-population/",
"Nigeria": "/world-population/nigeria-population/",
"Bangladesh": "/world-population/bangladesh-population/",
"Russia": "/world-population/russia-population/",
"Mexico": "/world-population/mexico-population/",
"Japan": "/world-population/japan-population/",
"Ethiopia": "/world-population/ethiopia-population/",
"Philippines": "/world-population/philippines-population/",
"Egypt": "/world-population/egypt-population/",
"Vietnam": "/world-population/vietnam-population/",
"DR Congo": "/world-population/democratic-republic-of-the-congo-population/",
"Turkey": "/world-population/turkey-population/",
"Iran": "/world-population/iran-population/",
"Germany": "/world-population/germany-population/",
"Thailand": "/world-population/thailand-population/",
"United Kingdom": "/world-population/uk-population/",
"France": "/world-population/france-population/",
"Italy": "/world-population/italy-population/",
"Tanzania": "/world-population/tanzania-population/",
"South Africa": "/world-population/south-africa-population/",
"Myanmar": "/world-population/myanmar-population/",
"Kenya": "/world-population/kenya-population/",
"South Korea": "/world-population/south-korea-population/",
"Colombia": "/world-population/colombia-population/",
"Spain": "/world-population/spain-population/",
"Uganda": "/world-population/uganda-population/",
"Argentina": "/world-population/argentina-population/",
"Algeria": "/world-population/algeria-population/",
"Sudan": "/world-population/sudan-population/",
"Ukraine": "/world-population/ukraine-population/",
"Iraq": "/world-population/iraq-population/",
"Afghanistan": "/world-population/afghanistan-population/",
"Poland": "/world-population/poland-population/",
"Canada": "/world-population/canada-population/",
"Morocco": "/world-population/morocco-population/",
"Saudi Arabia": "/world-population/saudi-arabia-population/",
"Uzbekistan": "/world-population/uzbekistan-population/",
"Peru": "/world-population/peru-population/",
"Angola": "/world-population/angola-population/",
"Malaysia": "/world-population/malaysia-population/",
"Mozambique": "/world-population/mozambique-population/",
"Ghana": "/world-population/ghana-population/",
"Yemen": "/world-population/yemen-population/",
"Nepal": "/world-population/nepal-population/",
"Venezuela": "/world-population/venezuela-population/",
"Madagascar": "/world-population/madagascar-population/",
"Cameroon": "/world-population/cameroon-population/",
"CÃ´te d'Ivoire": "/world-population/cote-d-ivoire-population/",
"North Korea": "/world-population/north-korea-population/",
"Australia": "/world-population/australia-population/",
"Niger": "/world-population/niger-population/",
"Taiwan": "/world-population/taiwan-population/",
"Sri Lanka": "/world-population/sri-lanka-population/",
"Burkina Faso": "/world-population/burkina-faso-population/",
"Mali": "/world-population/mali-population/",
"Romania": "/world-population/romania-population/",
"Malawi": "/world-population/malawi-population/",
"Chile": "/world-population/chile-population/",
"Kazakhstan": "/world-population/kazakhstan-population/",
"Zambia": "/world-population/zambia-population/",
"Guatemala": "/world-population/guatemala-population/",
"Ecuador": "/world-population/ecuador-population/",
"Syria": "/world-population/syria-population/",
"Netherlands": "/world-population/netherlands-population/",
"Senegal": "/world-population/senegal-population/",
"Cambodia": "/world-population/cambodia-population/",
"Chad": "/world-population/chad-population/",
"Somalia": "/world-population/somalia-population/",
"Zimbabwe": "/world-population/zimbabwe-population/",
"Guinea": "/world-population/guinea-population/",
"Rwanda": "/world-population/rwanda-population/",
"Benin": "/world-population/benin-population/",
"Burundi": "/world-population/burundi-population/",
"Tunisia": "/world-population/tunisia-population/",
"Bolivia": "/world-population/bolivia-population/",
"Belgium": "/world-population/belgium-population/",
"Haiti": "/world-population/haiti-population/",
"Cuba": "/world-population/cuba-population/",
"South Sudan": "/world-population/south-sudan-population/",
"Dominican Republic": "/world-population/dominican-republic-population/",
"Czech Republic (Czechia)": "/world-population/czech-republic-population/",
"Greece": "/world-population/greece-population/",
"Jordan": "/world-population/jordan-population/",
"Portugal": "/world-population/portugal-population/",
"Azerbaijan": "/world-population/azerbaijan-population/",
"Sweden": "/world-population/sweden-population/",
"Honduras": "/world-population/honduras-population/",
"United Arab Emirates": "/world-population/united-arab-emirates-population/",
"Hungary": "/world-population/hungary-population/",
"Tajikistan": "/world-population/tajikistan-population/",
"Belarus": "/world-population/belarus-population/",
"Austria": "/world-population/austria-population/",
"Papua New Guinea": "/world-population/papua-new-guinea-population/",
"Serbia": "/world-population/serbia-population/",
"Israel": "/world-population/israel-population/",
"Switzerland": "/world-population/switzerland-population/",
"Togo": "/world-population/togo-population/",
"Sierra Leone": "/world-population/sierra-leone-population/",
"Hong Kong": "/world-population/china-hong-kong-sar-population/",
"Laos": "/world-population/laos-population/",
"Paraguay": "/world-population/paraguay-population/",
"Bulgaria": "/world-population/bulgaria-population/",
"Libya": "/world-population/libya-population/",
"Lebanon": "/world-population/lebanon-population/",
"Nicaragua": "/world-population/nicaragua-population/",
"Kyrgyzstan": "/world-population/kyrgyzstan-population/",
"El Salvador": "/world-population/el-salvador-population/",
"Turkmenistan": "/world-population/turkmenistan-population/",
"Singapore": "/world-population/singapore-population/",
"Denmark": "/world-population/denmark-population/",
"Finland": "/world-population/finland-population/",
"Congo": "/world-population/congo-population/",
"Slovakia": "/world-population/slovakia-population/",
"Norway": "/world-population/norway-population/",
"Oman": "/world-population/oman-population/",
"State of Palestine": "/world-population/state-of-palestine-population/",
"Costa Rica": "/world-population/costa-rica-population/",
"Liberia": "/world-population/liberia-population/",
"Ireland": "/world-population/ireland-population/",
"Central African Republic": "/world-population/central-african-republic-population/",
"New Zealand": "/world-population/new-zealand-population/",
"Mauritania": "/world-population/mauritania-population/",
"Panama": "/world-population/panama-population/",
"Kuwait": "/world-population/kuwait-population/",
"Croatia": "/world-population/croatia-population/",
"Moldova": "/world-population/moldova-population/",
"Georgia": "/world-population/georgia-population/",
"Eritrea": "/world-population/eritrea-population/",
"Uruguay": "/world-population/uruguay-population/",
"Bosnia and Herzegovina": "/world-population/bosnia-and-herzegovina-population/",
"Mongolia": "/world-population/mongolia-population/",
"Armenia": "/world-population/armenia-population/",
"Jamaica": "/world-population/jamaica-population/",
"Qatar": "/world-population/qatar-population/",
"Albania": "/world-population/albania-population/",
"Puerto Rico": "/world-population/puerto-rico-population/",
"Lithuania": "/world-population/lithuania-population/",
"Namibia": "/world-population/namibia-population/",
"Gambia": "/world-population/gambia-population/",
"Botswana": "/world-population/botswana-population/",
"Gabon": "/world-population/gabon-population/",
"Lesotho": "/world-population/lesotho-population/",
"North Macedonia": "/world-population/macedonia-population/",
"Slovenia": "/world-population/slovenia-population/",
"Guinea-Bissau": "/world-population/guinea-bissau-population/",
"Latvia": "/world-population/latvia-population/",
"Bahrain": "/world-population/bahrain-population/",
"Equatorial Guinea": "/world-population/equatorial-guinea-population/",
"Trinidad and Tobago": "/world-population/trinidad-and-tobago-population/",
"Estonia": "/world-population/estonia-population/",
"Timor-Leste": "/world-population/timor-leste-population/",
"Mauritius": "/world-population/mauritius-population/",
"Cyprus": "/world-population/cyprus-population/",
"Eswatini": "/world-population/swaziland-population/",
"Djibouti": "/world-population/djibouti-population/",
"Fiji": "/world-population/fiji-population/",
"RÃ©union": "/world-population/reunion-population/",
"Comoros": "/world-population/comoros-population/",
"Guyana": "/world-population/guyana-population/",
"Bhutan": "/world-population/bhutan-population/",
"Solomon Islands": "/world-population/solomon-islands-population/",
"Macao": "/world-population/china-macao-sar-population/",
"Montenegro": "/world-population/montenegro-population/",
"Luxembourg": "/world-population/luxembourg-population/",
"Western Sahara": "/world-population/western-sahara-population/",
"Suriname": "/world-population/suriname-population/",
"Cabo Verde": "/world-population/cabo-verde-population/",
"Maldives": "/world-population/maldives-population/",
"Malta": "/world-population/malta-population/",
"Brunei ": "/world-population/brunei-darussalam-population/",
"Guadeloupe": "/world-population/guadeloupe-population/",
"Belize": "/world-population/belize-population/",
"Bahamas": "/world-population/bahamas-population/",
"Martinique": "/world-population/martinique-population/",
"Iceland": "/world-population/iceland-population/",
"Vanuatu": "/world-population/vanuatu-population/",
"French Guiana": "/world-population/french-guiana-population/",
"Barbados": "/world-population/barbados-population/",
"New Caledonia": "/world-population/new-caledonia-population/",
"French Polynesia": "/world-population/french-polynesia-population/",
"Mayotte": "/world-population/mayotte-population/",
"Sao Tome & Principe": "/world-population/sao-tome-and-principe-population/",
"Samoa": "/world-population/samoa-population/",
"Saint Lucia": "/world-population/saint-lucia-population/",
"Channel Islands": "/world-population/channel-islands-population/",
"Guam": "/world-population/guam-population/",
"CuraÃ§ao": "/world-population/curacao-population/",
"Kiribati": "/world-population/kiribati-population/",
"Micronesia": "/world-population/micronesia-country-population/",
"Grenada": "/world-population/grenada-population/",
"St. Vincent & Grenadines": "/world-population/saint-vincent-and-the-grenadines-population/",
"Aruba": "/world-population/aruba-population/",
"Tonga": "/world-population/tonga-population/",
"U.S. Virgin Islands": "/world-population/united-states-virgin-islands-population/",
"Seychelles": "/world-population/seychelles-population/",
"Antigua and Barbuda": "/world-population/antigua-and-barbuda-population/",
"Isle of Man": "/world-population/isle-of-man-population/",
"Andorra": "/world-population/andorra-population/",
"Dominica": "/world-population/dominica-population/",
"Cayman Islands": "/world-population/cayman-islands-population/",
"Bermuda": "/world-population/bermuda-population/",
"Marshall Islands": "/world-population/marshall-islands-population/",
"Northern Mariana Islands": "/world-population/northern-mariana-islands-population/",
"Greenland": "/world-population/greenland-population/",
"American Samoa": "/world-population/american-samoa-population/",
"Saint Kitts & Nevis": "/world-population/saint-kitts-and-nevis-population/",
"Faeroe Islands": "/world-population/faeroe-islands-population/",
"Sint Maarten": "/world-population/sint-maarten-population/",
"Monaco": "/world-population/monaco-population/",
"Turks and Caicos": "/world-population/turks-and-caicos-islands-population/",
"Saint Martin": "/world-population/saint-martin-population/",
"Liechtenstein": "/world-population/liechtenstein-population/",
"San Marino": "/world-population/san-marino-population/",
"Gibraltar": "/world-population/gibraltar-population/",
"British Virgin Islands": "/world-population/british-virgin-islands-population/",
"Caribbean Netherlands": "/world-population/caribbean-netherlands-population/",
"Palau": "/world-population/palau-population/",
"Cook Islands": "/world-population/cook-islands-population/",
"Anguilla": "/world-population/anguilla-population/",
"Tuvalu": "/world-population/tuvalu-population/",
"Wallis & Futuna": "/world-population/wallis-and-futuna-islands-population/",
"Nauru": "/world-population/nauru-population/",
"Saint Barthelemy": "/world-population/saint-barthelemy-population/",
"Saint Helena": "/world-population/saint-helena-population/",
"Saint Pierre & Miquelon": "/world-population/saint-pierre-and-miquelon-population/",
"Montserrat": "/world-population/montserrat-population/",
"Falkland Islands": "/world-population/falkland-islands-malvinas-population/",
"Niue": "/world-population/niue-population/",
"Tokelau": "/world-population/tokelau-population/",
"Holy See": "/world-population/holy-see-population/"
}



root = Tk()
root.title("World Population")
root.iconbitmap('pop.ico')
root.resizable(False, False)
country_frame = LabelFrame(root, text="World Population", padx=10, pady=10, font = ("Calibri", 13))
country_frame.grid(row=0, column=0, padx=20, pady=5, columnspan=4)
n = StringVar()
countrychoosen = ttk.Combobox(country_frame, width=50, state='readonly', textvariable=n, font = ("Calibri", 13))
countrychoosen['values'] = ('China', 'India', 'United States', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico', 'Japan', 'Ethiopia', 'Philippines', 'Egypt', 'Vietnam', 'DR Congo', 'Turkey', 'Iran', 'Germany', 'Thailand', 'United Kingdom', 'France', 'Italy', 'Tanzania', 'South Africa', 'Myanmar', 'Kenya', 'South Korea', 'Colombia', 'Spain', 'Uganda', 'Argentina', 'Algeria', 'Sudan', 'Ukraine', 'Iraq', 'Afghanistan', 'Poland', 'Canada', 'Morocco', 'Saudi Arabia', 'Uzbekistan', 'Peru', 'Angola', 'Malaysia', 'Mozambique', 'Ghana', 'Yemen', 'Nepal', 'Venezuela', 'Madagascar', 'Cameroon', "CÃ´te d'Ivoire", 'North Korea', 'Australia', 'Niger', 'Taiwan', 'Sri Lanka', 'Burkina Faso', 'Mali', 'Romania', 'Malawi', 'Chile', 'Kazakhstan', 'Zambia', 'Guatemala', 'Ecuador', 'Syria', 'Netherlands', 'Senegal', 'Cambodia', 'Chad', 'Somalia', 'Zimbabwe', 'Guinea', 'Rwanda', 'Benin', 'Burundi', 'Tunisia', 'Bolivia', 'Belgium', 'Haiti', 'Cuba', 'South Sudan', 'Dominican Republic', 'Czech Republic (Czechia)', 'Greece', 'Jordan', 'Portugal', 'Azerbaijan', 'Sweden', 'Honduras', 'United Arab Emirates', 'Hungary', 'Tajikistan', 'Belarus', 'Austria', 'Papua New Guinea', 'Serbia', 'Israel', 'Switzerland', 'Togo', 'Sierra Leone', 'Hong Kong', 'Laos', 'Paraguay', 'Bulgaria', 'Libya', 'Lebanon', 'Nicaragua', 'Kyrgyzstan', 'El Salvador', 'Turkmenistan', 'Singapore', 'Denmark', 'Finland', 'Congo', 'Slovakia', 'Norway', 'Oman', 'State of Palestine', 'Costa Rica', 'Liberia', 'Ireland', 'Central African Republic', 'New Zealand', 'Mauritania', 'Panama', 'Kuwait', 'Croatia', 'Moldova', 'Georgia', 'Eritrea', 'Uruguay', 'Bosnia and Herzegovina', 'Mongolia', 'Armenia', 'Jamaica', 'Qatar', 'Albania', 'Puerto Rico', 'Lithuania', 'Namibia', 'Gambia', 'Botswana', 'Gabon', 'Lesotho', 'North Macedonia', 'Slovenia', 'Guinea-Bissau', 'Latvia', 'Bahrain', 'Equatorial Guinea', 'Trinidad and Tobago', 'Estonia', 'Timor-Leste', 'Mauritius', 'Cyprus', 'Eswatini', 'Djibouti', 'Fiji', 'RÃ©union', 'Comoros', 'Guyana', 'Bhutan', 'Solomon Islands', 'Macao', 'Montenegro', 'Luxembourg', 'Western Sahara', 'Suriname', 'Cabo Verde', 'Maldives', 'Malta', 'Brunei ', 'Guadeloupe', 'Belize', 'Bahamas', 'Martinique', 'Iceland', 'Vanuatu', 'French Guiana', 'Barbados', 'New Caledonia', 'French Polynesia', 'Mayotte', 'Sao Tome & Principe', 'Samoa', 'Saint Lucia', 'Channel Islands', 'Guam', 'CuraÃ§ao', 'Kiribati', 'Micronesia', 'Grenada', 'St. Vincent & Grenadines', 'Aruba', 'Tonga', 'U.S. Virgin Islands', 'Seychelles', 'Antigua and Barbuda', 'Isle of Man', 'Andorra', 'Dominica', 'Cayman Islands', 'Bermuda', 'Marshall Islands', 'Northern Mariana Islands', 'Greenland', 'American Samoa', 'Saint Kitts & Nevis', 'Faeroe Islands', 'Sint Maarten', 'Monaco', 'Turks and Caicos', 'Saint Martin', 'Liechtenstein', 'San Marino', 'Gibraltar', 'British Virgin Islands', 'Caribbean Netherlands', 'Palau', 'Cook Islands', 'Anguilla', 'Tuvalu', 'Wallis & Futuna', 'Nauru', 'Saint Barthelemy', 'Saint Helena', 'Saint Pierre & Miquelon', 'Montserrat', 'Falkland Islands', 'Niue', 'Tokelau', 'Holy See')
countrychoosen.grid(row=0, column=0, columnspan=4, padx = 10, pady=10)
countrychoosen.current(0)

years = [2020,
         2019,
         2018,
         2017,
         2016,
         2015,
         2010,
         2005,
         2000,
         1995,
         1990,
         1985,
         1980,
         1975,
         1970,
         1965,
         1960,
         1955]

year = IntVar()
year.set(years[-1])
drop_down = OptionMenu(country_frame, year, *years)
drop_down.grid(row=1, column=3, columnspan=1, padx=10)
drop_down.config(width=8, fg='white', bg='black', font = ("Calibri", 12))
year.set(years[0])

popLabel=Label(country_frame, text="", font = ("Calibri", 50))
popLabel.grid(row=2, column=0, columnspan=4)

def searchcountry():
    global uurl
    global lab
    global popLabel
    popLabel.grid_forget()
    d = {}
    l = []
    uurl = str(n.get())
    curl = 'https://www.worldometers.info'+clink[uurl]
    page = requests.get(curl)
    soup = BeautifulSoup(page.text, 'html.parser')
    for i in soup.select('strong')[10:28]:
        l.append(i.get_text())

    for i in range(len(l)):
        d[f'{years[i]}'] = str(l[i])
    res = d[str(year.get())]
    popLabel=Label(country_frame, text=str(res), font = ("Calibri", 40))
    popLabel.grid(row=2, column=0, columnspan=4)





searchBtn = Button(country_frame, text="Search", bg='black', fg='white', width = 13, font = ("Calibri", 11),command=searchcountry)
searchBtn.grid(row = 1, column=0, columnspan=1,pady=10)


















Label(root, text='Project by Subareesh', fg='red').grid(row=1, column=0, columnspan=4, pady=5)
root.mainloop()
