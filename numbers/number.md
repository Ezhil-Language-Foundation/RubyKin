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

ரூபி கணித, ஏரணச் செயல்பாடுகளைச் செய்யும் ஆற்றல்பெற்றது. 
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

இக்கட்டளைகளை ரூபி இயக்கியில் நீங்கள் செயல்படுத்த, ரூபியை உங்கள் கணினியில் நிறுவ வேண்டும். 

__ரூபியினை நிறுவுதல் __ 

நீங்கள்  OS X இணை பயன்படுத்துகிறீர்கள் என்றால், அதில் ரூபி ஏற்கனவே நிறுவப்பட்டிருக்கும். இப்போது உங்களுடைய Terminal application திறக்கவும். இதனை கண்டுபிடிக்க திரையின் வலது மேல் மூலையில் உள்ள magnifying glass(பூதக் கண்ணாடி) பொத்தானை அழுத்தவும். பின் Terminal என தட்டச்சு செய்து முதலாவது விளைவை தெரிவு செய்க. (இல்லையெனில் நீங்கள்  Applications - Utilities - Terminal என்பதன் ஊடாக சென்று இரு தடவை terminal ல் அழுத்தி திறக்க முடியும்.)

![to open Terminal on a Mac](http://rubykin.com/images/terminal_directions.png) 

நீங்கள் Linux பாவிப்பவாராக இருந்தால், ஒரு shell இனை திறந்து, irb என தட்டச்சு செய்து enter இனை அழுத்தவும். மேலும் நீங்கள் Windows பாவிப்பவர் என்றால், Ruby பகுதியிலுள்ள Start Menuல் உள்ள fxri இனை திறக்கவும். மூன்றாம் தெரிவாக Repl.it (http://repl.it/languages/Ruby) என்பதனை தேடிப்பார்க்கவும். இது ஒரு அற்புதமான இலகுவான கருவி. இது தேடல் பொறிகளில் நிரலாக்கம்  எழுத உங்களை அனுமதிக்கிறது. இங்கு நிறுவுதல் அவசியம் இல்லை.
 

அடுத்து irb என terminal அல்லது shell திரையில் தட்டச்சு செய்து enter இனை அழுத்தவும். 

__IRB என்றால் என்ன?__ 

IRB என்பது Interactive Ruby Shell என்பதன் சுருக்கம் ஆகும். IRB என்பது உங்கள் கணினியில் உள்ள ஒரு சிறு இரகசிய கோட்டைபோன்றது. நீங்கள் உங்கள் IRB சூழ்நிலையை பயன்படுத்தி Ruby பற்றி அறிந்து கொள்ளவும் மற்றும் வெவ்வேறான  கட்டளைகளை தெரிந்து கொள்ளவும் முடியும். IRB யை திறந்து (shell window அல்லது www.repl.it/languages/Ruby பாவித்து திறக்கவும்) கீழ் தரப்படமாதிரி சில எளிய கணகீடுகளை தட்டச்சு செய்து என்ன மாதிரியான வெளியீடுகளை கணணி தருகின்றது என்பதை பார்க்கவும். அல்லது சுயமாக முயற்சி செய்து பார்க்கவும். 

```ruby 
2 + 2 
4 < 7 
5 > 10 
7 / 4 
``` 

Arrows => பற்றி அறிய ஆர்வமாக உள்ளதா? Ruby பொறியியலாளர்கள் இதனை எண்ணிம அடைவு ராக்கட் என அழைக்க விரும்புவார்கள். IRBனுள் 3 + 2 என தட்டச்சு செய்தாலோ அல்லது வேறு வகையான காரணிகளை உள்ளீடு செய்தாலோ எப்போதும் அது சுட்டியால் => குறிப்பிடப்பட்ட ஒரு மதிப்பை விளைவாக தரும்.

/> __சிறு துளி கணிதம்__ 

ரூபி போன்ற நிரல்மொழிகள் பல மடங்கு பெரிய கணித கணக்குகளை இயக்கவல்லது. நமக்குச் சலிக்கும் ஆனால், கணினி சலிக்காமல், சளைக்காமல் வேலை செய்து விடை சொல்லும். இந்தப் பக்கத்தில் அடுத்து, வகுத்தல்மீதம் (modulo), மற்றும் அடுக்குக்குறி (exponent) ஆகிய கணித செயல்பாடுகளை ரூபி எவ்வாறு கையாள்கிறது என்று பார்ப்போம்! 


__அடுக்குக்குறி__ 

அடுக்குக்குறி ஒர் எண் எவ்வளவுமுறை பெருக்கப்பட வேண்டும் என்று கூறும். எ.கா. 2 பெருக்கல் 2 என்பது 4. 4 பெருக்கல் 2 என்பது 8. அதாவது 2^3 என்றால் 2 பெருக்கல் 2 பெருக்கல் 2 , என்பதின் விடை 8

அடுக்குக்குறி பற்றி அறிந்தால்தான், ரூபியில் நிரலாக்கம் செய்யலாம் என்றில்லை. ரூபி இரண்டு பெருக்கல்குறியை கொண்டு அடுக்குக்குறியை குறியிடும்.
 


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

வகுத்தல்மீதம் மற்றும் அடுக்குக்குறி சற்று சிக்கலாக இருந்தால் கவலைபட வேண்டாம். நிரலாக்கம் செய்ய இவை கட்டாயமா தேவையில்லை. 

தற்போதைக்கு, கணினி உங்களுக்காகக் கணித செயல்பாடுகளைச் செய்யும் என்ற அடிப்படையைப் புரிந்தாலே, சிறப்பு. 
