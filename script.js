let original_text = `ROCHESTER HILLS, Mich., Nov. 27, 2017 – FANUC CORPORATION, the world's leading supplier of robotics, CNC and factory automation has announced the production of its 500,000th robot.
<br><br>
'Automation and robotics are key drivers of manufacturing competitiveness,' said Mike Cicco, president & CEO, FANUC America.  'More companies are using automation to overcome inefficiencies, lower costs, increase productivity, and gain market share. Having sold a half million robots is a key milestone for FANUC, and we're looking forward to expanding our capabilities to keep pace with the growing demand for automation.'  
<br><br>
In April, FANUC announced plans to build a new factory scheduled to open in August 2018. FANUC's new factory will increase its robot capacity from 6,000 to 11,000 units per month. 
<br><br>
'The backbone of FANUC's success is our talented workforce – all automation professionals, including an expanding product development team based in Japan and the U.S.,' Cicco added. 'In addition to highly qualified employees, we offer the most reliable automation products in the marketplace.  Everyone at FANUC is very motivated and focused on designing the hardware and software that make our products easy to learn and use for all manufacturers, including the practical application of IIoT technologies.'
`

let corrected_text = original_text.replace(/\B'|'\B/gm, '"')

let orig = document.getElementById('orig')
orig.innerHTML = original_text
let cor = document.getElementById('cor')
cor.innerHTML = corrected_text