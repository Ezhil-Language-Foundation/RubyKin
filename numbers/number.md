# எண்கள் 

உங்களுக்குக் கூட்டல், கழித்தல், பெருக்கல், வகுத்தல் எல்லாம் தெரியுமா ? சபாஷ், ரூபி மொழிக்கும் அதெல்லாம் தெரியும்! 

```ruby 
2 + 2 => 4 
9 - 3 => 6 
2 * 3 => 6 
4 / 2 => 2 
``` 

> செயல்பாடு = Operation 
> ஏரணம் = logic 

ரூபி-யால் கணித, ஏரணச் செயல்பாடுகளைச் செய்யும் ஆற்றல்பெற்றது. 
`எ.கா.` 

- **`+`** கூட்டல் 
- **`-`** கழித்தல் 
- **`>`** பெரியதா? 
- **`<`** சிறியதா? 

```ruby 
4 > 2 => true ( மெய் ) 
7 < 2 => false (பொய் ) 
3 >= 3 => true ( மெய் ) 
0 <= 1 => true ( மெய் ) 
``` 

இக்கட்டளைகளை ரூபி இயக்கியில் நீங்கள் செயல்படுத்த, ரூபி-யை உங்கள் கணினியில் நிறுவ வேண்டும். 

__Installing Ruby__ 

If you’re using Mac OS X, Ruby is already installed. Hooray! Just open your _Terminal_ application. To find terminal you can click the magnifying glass in the top right corner of your screen, then type Terminal and click the first result. (Or you can navigate to Applications - Utilities - Terminal and double click). 

![to open Terminal on a Mac](http://rubykin.com/images/terminal_directions.png) 

If you’re using Linux, open up a shell, type irb and hit enter. 
And if you’re on Windows, open fxri from the Ruby section of your Start Menu. 

As a third option, check out Repl.it (http://repl.it/languages/Ruby). This is a pretty fantastic tool that allows you to type code into your web browser. No installation required! 

Next, type the letters `irb` into the terminal or shell screen and hit enter. 

__IRB என்றால் என்ன?__ 

IRB stands for Interactive Ruby Shell. An Interactive Ruby Shell is like a little secret fort located inside your computer. You can use your IRB environment to play around with Ruby and learn different commands. Open up IRB (from a shell window or using www.repl.it/languages/Ruby and try typing some of these simple math calculations to see what the computer returns. Or try your own! 

```ruby 
2 + 2 
4 < 7 
5 > 10 
7 / 4 
``` 

Curious about the `=>` arrows? Ruby engineers like to call these hash rockets. You will see that typing `3 + 2` or any other thing into IRB will always return a value, signified by the pointer `=>`. 

/> 
__சிறு துளி கணிதம்__ 

ரூபி போன்ற நிரல்மொழிகள் _பல மடங்கு_ பெரிய கணித கணக்குகளை இயக்கவல்லது. நமக்குச் சலிக்கும் ஆனால், கணினி சலிக்காமல், சளைக்காமல் வேலை செய்து விடை சொல்லும். இந்தப் பக்கத்தில் அடுத்து, வகுத்தல்மீதம் (modulo), மற்றும் அடுக்குக்குறி (exponent) ஆகிய கணித செயல்பாடுகளை ரூபி கையாள்கிறது என்று பார்ப்போம்! 


__அடுக்குக்குறி__ 

அடுக்குக்குறி ஒர் எண் எவ்வளவுமுறை பெருக்கப்பட வேண்டும் என்று கூறும். 
`எ.கா.` 2 பெருக்கல் 2 என்பது 4. 4 பெருக்கல் 2 என்பது 8. அதாவது 2^3 என்றால் 2 பெருக்கல் 2 பெருக்கல் 2 , என்பதின் விடை 8 

அடக்குக்குறி பற்றி அறிந்தால்தான், ரூபியில் நிரலாக்கம் செய்யலாம் என்றில்லை. 
ரூபி இரண்டு பெருக்கல்குறியை கொண்டு அடுக்குக்குறியை குறியிடும். 


```ruby 
2 ** 3 => 8 
3 ** 2 => 9 
10 ** 3 => 1000 #10 முறை 10 முறை 10! 
# குறி , குறிப்புரை எழுத உதவும் 
# (ரூபி இக்குறி உள்ள வரியை பொருட்படுத்தாது.) 
``` 

__வகுத்தல்மீதம்__ 

இயல்பான கணித செயல்பாடுகள் இல்லாமல், கணினியில் `வகுத்தல்மீதம்` என்ற ஒரு செயல்பாடு உண்டு. அச்செயல்பாட்டை **%** குறிக்கும். 

இச்செயல்பாடு ஒர் எண்ணை மற்றொரு எண்ணால் வகுக்கும் போது கிடைக்கும் மீதத்தைத் தரும். `எ.கா.` 

- 9 என்ற எண்ணை மூன்றால் சரியாக வகுபடும், அதாவது மீதம் 0. அதனால் 9 % 3 என்பது 0. 
- 9 என்ற எண்ணைஇரண்டால் வகுத்தால் அதாவது மீதம் 1. அதனால் 9 % 
2 என்பது 1. 

பின்வரும் எடுத்துகாட்டுகளை முயலுங்கள் 

```ruby 
8 % 2 => 0 
9 % 2 => 1 
9 % 5 => 4 
``` 

வகுத்தல்மீதம் மற்றும் அடுக்குக்குறி சற்று சிக்கலா இருக்ககிற மாதிரி இருந்தால் கவலைபட வேண்டாம். நிரலாக்கம் செய்ய இவை கட்டாயமா தேவையில்லை. 

தற்போதைக்கு, கணினி உங்களுக்காகக் கணித செயல்பாடுகளைச் செய்யும் என்ற அடிப்படையைப் புரிந்தாலே, சிறப்பு. 
