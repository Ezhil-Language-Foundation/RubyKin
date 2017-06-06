# எண்கள்

உங்களுக்கு கூட்டல், கழித்தல், பெருக்கல், வகுத்தல் எல்லாம் தெரியுமா ? சபாஷ், ரூபி மொழிக்கும் அதெல்லாம் தெரியும்! நீங்கள் எப்படி இந்த கூட்டல், கழித்தல், பெருக்கல், வகுத்தல் எல்லாம் செய்வீங்களோ அதேமாதிரி ரூபியும் செய்யும்.

  ```ruby
  2 + 2 => 4
  9 - 3 => 6
  2 * 3 => 6
  4 / 2 => 2
  ```

ரூபி தர்க ரீதியான பெரியது  `>` and கம்மியானது `<` செயலுறுப்புகளையும் பிரியும்; செயலுருபு என்ற ஒரு கணிதம் அல்ல கணினி செயல் என்று பொருள் -  கூட்டல், கழித்தல் எல்லாம் ஒரு செயலுருபு என்றும் சொல்லலாம்.

  ```ruby
  4 > 2 => மெய் 
  7 < 2 => பொய்
  3 >= 3 => மெய்
  0 <= 1 => மெய்
  ```
  
  நீங்களே இந்த கட்டளைகளை ரூபி இயக்கியில் செயல்படுத்தலாம் - அனால் அதற்க்கு ரூபி உங்கள் கணினியில் நிறுவ பட வேண்டும்.

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

<br />
__சிறு துளி கணிதம்__

ரூபி போன்ற நிரல் மொழிகள் _பல மடங்கு_ பெரிய கணித கணக்குகளை இயக்கம் தன்மை கொண்டது; நமக்கு சலித்து போகும் படி கணினி சலிக்காமல், சளைக்காமல் வேலை செய்து விடை சொல்லும். இந்த பக்கத்தில் அடுத்த கட்டமான கணித செயலுறுப்புகளை வகுத்தல்மீதம் (modulo), மற்றும் அடுக்குக்குறி (exponent)-களை ரூபி கையாள்கிறது என்று பார்ப்போம்!


__அடுக்குக்குறி__

Exponents tell a number how many times it should be multiplied. For example, 2 times 2 equals 4, 4 times 2 equals 8. So, 2^3 means 2 times 2 times 2, or 8. Don't worry about exponents if they are unfamiliar to you. They are not necessary to learn programming! Ruby uses two stars to signify an exponent math expression:

  ```ruby
  2 ** 3 => 8
  3 ** 2 => 9
  10 ** 3 => 1000  #10 times 10 times 10!
  # Also, the pound symbol is used for comments
  # (and ignored by Ruby)
  ```


__வகுத்தல்மீதம்__

In addition to these standard math operations, the computer has something called the modulo operator, which is represented using a percent symbol: %. The modulo’s job is to find the remainder after dividing one number with another. The remainder is what is left over, or what remains when you divide one big number by a smaller number. Let's look at an example.

9 divided by 3 would result in a modulo of 0, because there is no remainder. Since 3 divides evenly into 9 (three times) there are no numbers left over, and that is why 9 modulo 3 is 0. If we try it again with a different set of numbers, say 9 modulo 2, we would have a remainder (or a modulo operator) of 1. Because 9 divided by 2 equals 8, leaving a remainder of 1. Try these examples

  ```ruby
  8 % 2 => 0
  9 % 2 => 1
  9 % 5 => 4
  ```

If exponents and modulos are too complex to understand right now, don't worry. Again, they are not a requirement for programming. It's important at this stage to simply understand that the computer can do simple math for you. Check out some examples below.

<div style="height:30px;"></div>
