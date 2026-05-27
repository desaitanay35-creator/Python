import pandas as pd 
import requests as rs
from bs4 import BeautifulSoup
from django.shortcuts import render
def dataframes(request):
    with open('app1/demo.html','r',encoding='utf-8') as f:
        res= f.read()
    soup = BeautifulSoup(res,'html.parser')
    box=soup.find_all('div',class_="yKfJKb row")
    d={'name':[],'Rom':[],'Ram':[],'Color':[],'stars':[], 'Reviews':[],'Rear camera':[],'Front Camera':[],'Old Price':[],'New Price':[],'Discount':[],'Display(cm)':[],'Display(in)':[]}
    for i in box:
        try:
            d['name'].append(i.find('div',class_='KzDlHZ').text.split('(')[0].strip())
            d['Rom'].append(i.find('li',class_='J+igdf').text.split('|')[0].strip())
            d['Ram'].append("Ram "+i.find('div',class_='KzDlHZ').text.split(',')[-1].strip(')'))
            d['Color'].append(i.find('div',class_='KzDlHZ').text.split('(')[1].split(',')[0])
            d['stars'].append(i.find('div',class_='XQDdHH').text.strip())
            d['Reviews'].append(i.find('span',class_="Wphh3N").text.split('&')[1].strip())
            d['Rear camera'].append(i.find('li',class_="J+igdf").text.split('|')[1].split('Display')[1].strip())
            d['Front Camera'].append(i.find('li',class_="J+igdf").text.split('|')[2].split('Camera')[0].strip())
            d['Display(cm)'].append(i.find('li',class_="J+igdf").text.split('ROM')[1].split('(')[0].strip())
            d['Display(in)'].append(i.find('li',class_="J+igdf").text.split('(')[1].split(')')[0].strip())
        except:
            d['name'].append('NaN')
            d['Rom'].append('NaN')
            d['Ram'].append('NaN')
            d['Color'].append('NaN')
            d['stars'].append('NaN')
            d['Rear camera'].append('NaN')
            d['Front Camera'].append('NaN')
            d['Display(cm)'].append('NaN')
            d['Display(in)'].append('NaN')
            
        
        
            
        try:
            d['Old Price'].append(i.find('div',class_="yRaY8j ZYYwLA").text.split('₹')[1].strip())
        except:
            d['Old Price'].append('NaN')
        try:
            d['New Price'].append(i.find('div',class_="Nx9bqj _4b5DiR").text.split('₹')[1].strip())
        except:
            d['New Price'].append('NaN')
            
        try:
            d['Discount'].append(i.find('div',class_="UkUFwK").text.strip())
            
        except:
            d['Discount'].append('NaN')
            
            # d['Display(cm)'].append('NaN')
            # d['Display(in)'].append('NaN')
            # d['Discount'].append('NaN')
            
    
    df= pd.DataFrame(d)    
        
    return render(request,'home.html',{'df':df})
# Create your views here.

