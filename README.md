<div class="relative default font-sans text-base text-textMain dark:text-textMainDark selection:bg-superDuper selection:text-textMain"><div class="min-w-0 break-words [word-break:break-word]"><div dir="auto"><div class="prose dark:prose-invert inline leading-normal break-words min-w-0 [word-break:break-word]"><h3>QRCode Generator MTB</h3>
<span class="">This project is a simple QR code generator web application built using Flask. Users can input a URL, and the application will generate a QR code for that URL. Additionally, the application allows users to download the generated QR code.</span>
<h3>Features</h3>
<ul class="list-outside list-disc pl-8">
<li><span class="">Generate QR codes for URLs</span></li>
<li><span class="">Download generated QR codes</span></li>
<li><span class="">Beautiful background image rotation</span></li>
<li><span class="">Activity logging for requests and errors</span></li>
<li><span class="">Tiny footer text "Ayan@M&amp;T" in the bottom right corner</span></li>
</ul>
<h3>Installation</h3>
<ol class="list-outside list-decimal marker:font-mono marker:text-sm pl-11">
<li><span class="">Clone the repository:</span><span class="">
</span><span class=""><div class="w-full  max-w-[90vw]"><pre class="not-prose font-mono font-extralight rounded overflow-hidden w-full text-sm"><div class="relative codeWrapper my-md"><div class="absolute text-textMainDark" style="z-index: 1; left: 0.75em; top: 10px;">bash</div><div class="sc-gEvEer ePundr"><span style="font-size: inherit; font-family: inherit; background: rgb(45, 45, 45); color: rgb(204, 204, 204); border-radius: 3px; display: flex; line-height: 1.42857; overflow-x: auto; white-space: pre;"><code style="font-size: inherit; font-family: inherit; line-height: 1.66667; padding: 8px;"><span class="token" style="color: rgb(204, 204, 204);">git</span> clone https://github.com/your-username/QRCode-generator-mtb.git
</code></span><button type="button" class="sc-aXZVg hebEKa"><svg class="icon" viewBox="0 0 384 512" width="16pt" height="16pt" fill="#cccccc"><path d="M280 240H168c-4.4 0-8 3.6-8 8v16c0 4.4 3.6 8 8 8h112c4.4 0 8-3.6 8-8v-16c0-4.4-3.6-8-8-8zm0 96H168c-4.4 0-8 3.6-8 8v16c0 4.4 3.6 8 8 8h112c4.4 0 8-3.6 8-8v-16c0-4.4-3.6-8-8-8zM112 232c-13.3 0-24 10.7-24 24s10.7 24 24 24 24-10.7 24-24-10.7-24-24-24zm0 96c-13.3 0-24 10.7-24 24s10.7 24 24 24 24-10.7 24-24-10.7-24-24-24zM336 64h-80c0-35.3-28.7-64-64-64s-64 28.7-64 64H48C21.5 64 0 85.5 0 112v352c0 26.5 21.5 48 48 48h288c26.5 0 48-21.5 48-48V112c0-26.5-21.5-48-48-48zM192 48c8.8 0 16 7.2 16 16s-7.2 16-16 16-16-7.2-16-16 7.2-16 16-16zm144 408c0 4.4-3.6 8-8 8H56c-4.4 0-8-3.6-8-8V120c0-4.4 3.6-8 8-8h40v32c0 8.8 7.2 16 16 16h160c8.8 0 16-7.2 16-16v-32h40c4.4 0 8 3.6 8 8v336z"></path></svg></button></div></div></pre></div></span><span class="">
</span></li>
<li><span class="">Install the required dependencies:</span><span class="">
</span><span class=""><div class="w-full  max-w-[90vw]"><pre class="not-prose font-mono font-extralight rounded overflow-hidden w-full text-sm"><div class="relative codeWrapper my-md"><div class="absolute text-textMainDark" style="z-index: 1; left: 0.75em; top: 10px;">bash</div><div class="sc-gEvEer ePundr"><span style="font-size: inherit; font-family: inherit; background: rgb(45, 45, 45); color: rgb(204, 204, 204); border-radius: 3px; display: flex; line-height: 1.42857; overflow-x: auto; white-space: pre;"><code style="font-size: inherit; font-family: inherit; line-height: 1.66667; padding: 8px;">pip <span class="token" style="color: rgb(204, 204, 204);">install</span> flask qrcode<span class="token punctuation">[</span>pil<span class="token punctuation">]</span>
</code></span><button type="button" class="sc-aXZVg hebEKa"><svg class="icon" viewBox="0 0 384 512" width="16pt" height="16pt" fill="#cccccc"><path d="M280 240H168c-4.4 0-8 3.6-8 8v16c0 4.4 3.6 8 8 8h112c4.4 0 8-3.6 8-8v-16c0-4.4-3.6-8-8-8zm0 96H168c-4.4 0-8 3.6-8 8v16c0 4.4 3.6 8 8 8h112c4.4 0 8-3.6 8-8v-16c0-4.4-3.6-8-8-8zM112 232c-13.3 0-24 10.7-24 24s10.7 24 24 24 24-10.7 24-24-10.7-24-24-24zm0 96c-13.3 0-24 10.7-24 24s10.7 24 24 24 24-10.7 24-24-10.7-24-24-24zM336 64h-80c0-35.3-28.7-64-64-64s-64 28.7-64 64H48C21.5 64 0 85.5 0 112v352c0 26.5 21.5 48 48 48h288c26.5 0 48-21.5 48-48V112c0-26.5-21.5-48-48-48zM192 48c8.8 0 16 7.2 16 16s-7.2 16-16 16-16-7.2-16-16 7.2-16 16-16zm144 408c0 4.4-3.6 8-8 8H56c-4.4 0-8-3.6-8-8V120c0-4.4 3.6-8 8-8h40v32c0 8.8 7.2 16 16 16h160c8.8 0 16-7.2 16-16v-32h40c4.4 0 8 3.6 8 8v336z"></path></svg></button></div></div></pre></div></span><span class="">
</span></li>
</ol>
<h3>Usage</h3>
<ol class="list-outside list-decimal marker:font-mono marker:text-sm pl-11">
<li><span class="">Run the Flask application:</span><span class="">
</span><span class=""><div class="w-full  max-w-[90vw]"><pre class="not-prose font-mono font-extralight rounded overflow-hidden w-full text-sm"><div class="relative codeWrapper my-md"><div class="absolute text-textMainDark" style="z-index: 1; left: 0.75em; top: 10px;">bash</div><div class="sc-gEvEer ePundr"><span style="font-size: inherit; font-family: inherit; background: rgb(45, 45, 45); color: rgb(204, 204, 204); border-radius: 3px; display: flex; line-height: 1.42857; overflow-x: auto; white-space: pre;"><code style="font-size: inherit; font-family: inherit; line-height: 1.66667; padding: 8px;">python app.py
</code></span><button type="button" class="sc-aXZVg hebEKa"><svg class="icon" viewBox="0 0 384 512" width="16pt" height="16pt" fill="#cccccc"><path d="M280 240H168c-4.4 0-8 3.6-8 8v16c0 4.4 3.6 8 8 8h112c4.4 0 8-3.6 8-8v-16c0-4.4-3.6-8-8-8zm0 96H168c-4.4 0-8 3.6-8 8v16c0 4.4 3.6 8 8 8h112c4.4 0 8-3.6 8-8v-16c0-4.4-3.6-8-8-8zM112 232c-13.3 0-24 10.7-24 24s10.7 24 24 24 24-10.7 24-24-10.7-24-24-24zm0 96c-13.3 0-24 10.7-24 24s10.7 24 24 24 24-10.7 24-24-10.7-24-24-24zM336 64h-80c0-35.3-28.7-64-64-64s-64 28.7-64 64H48C21.5 64 0 85.5 0 112v352c0 26.5 21.5 48 48 48h288c26.5 0 48-21.5 48-48V112c0-26.5-21.5-48-48-48zM192 48c8.8 0 16 7.2 16 16s-7.2 16-16 16-16-7.2-16-16 7.2-16 16-16zm144 408c0 4.4-3.6 8-8 8H56c-4.4 0-8-3.6-8-8V120c0-4.4 3.6-8 8-8h40v32c0 8.8 7.2 16 16 16h160c8.8 0 16-7.2 16-16v-32h40c4.4 0 8 3.6 8 8v336z"></path></svg></button></div></div></pre></div></span><span class="">
</span></li>
<li><span class="">Access the application in your browser at </span><span class=""><code>http://localhost:5000</code></span></li>
</ol>
<h3>Screenshots</h3>
<span class=""><img width="500" alt="image" src="https://github.com/ayananshu/QRCode-generator-mtb/assets/30047668/519d7709-ea7b-4c07-baa9-cde526f3be42">
<br></span><span class="">
<span class=""><img width="500" alt="Screenshot 2024-02-27 at 11 49 09 AM" src="https://github.com/ayananshu/QRCode-generator-mtb/assets/30047668/d53e9c67-cbb8-412e-96de-c6e86c1979c7">
</span>span>
<h3>Credits</h3>
<ul class="list-outside list-disc pl-8">
<li><span class="">QR code generation powered by the </span><span class=""><code>qrcode</code></span><span class=""> library</span></li>
<li><span class="">Background image rotation inspired by web design trends</span></li>
</ul>
<h3>License</h3>
<span class="">This project is licensed under the MIT License - see the </span><span class=""><a target="_blank" class="break-word decoration-from-font underline underline-offset-1 hover:text-super hover:decoration-super dark:hover:text-superDark dark:hover:decoration-superDark transition-all duration-300" href="/LICENSE">LICENSE</a></span><span class=""> file for details.</span><span class="block mt-md"></span>
<span class="">Feel free to contribute to this project by submitting pull requests or opening issues. Thank you for checking out QRCode Generator MTB! 🚀</span></div></div></div></div>
