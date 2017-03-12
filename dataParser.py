import urllib2       
    
def crawls_through_source():
    
    fo = open('generated.txt', 'w+')
    
    pages = ['1', '2', '3', '4', '5']
    pageChanger = 0
    
    while True:
        seed = 'http://dinosaurs.about.com/od/typesofdinosaurs/a/dinosaursatoz_%s.htm' % pages[pageChanger]
        #seed is the website where the data is being obtained
        
        pageChanger += 1
        #page changer goes through the list called pages[] and changes the number inside 
        
        response = urllib2.urlopen(seed)
        #gets response from the site
        
        page_source = response.read()
        #gets the source code of the site
        
        lookFor = 0
        
        while True:
            #this loop updates the variable lookFor so that 
            #it automates the finding of words to parse
            #read how the find() function works
            #it will help you understand these 2 loops better
            
            toLook = 'data-component="link" data-source="inlineLink" data-type="internalLink" data-ordinal="'
            #toLook is what we want to find in the source code
            
            lookFor = page_source.find('data-component="link" data-source="inlineLink" data-type="internalLink" data-ordinal="', lookFor) + 3
            #lookFor is going to be a number
            #the long line says page_source.find(toLook, lookFor)
            
            stopLooking = page_source.find('<', lookFor)
            
            #print page_source[lookFor + len(toLook)  : stopLooking] 
            #this line was commented out, it was there for debugging purposes
            
            fo.write(page_source[lookFor + len(toLook)  : stopLooking])
            fo.write('\n')
            #this last part generates a list so that we can obtain data 
            #by telling it from the point we want start getting data
            #to the point we wanted to stop
            
            if lookFor == -1 + 3:
                break
        if pageChanger > 4:
            break
    pageChanger += 1                                  
    fo.close()
                
def main():
    crawls_through_source()
    
    
if __name__== "__main__":
    main()
