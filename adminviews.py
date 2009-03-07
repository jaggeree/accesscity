import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext import db

from xml.dom import minidom

import models
import helpers
import viewhelpers

class MainHandler(webapp.RequestHandler):
	def get(self):
		template_values = {
		}
		viewhelpers.render_template(self, "adminviews/home", template_values)


class DataLoadHandler(webapp.RequestHandler):
	def get(self):
		rawresponse = """
		<tubes>
<tube><option value="2">Acton Town Tube Station</option></tube>
<tube><option value="3">Aldgate Tube Station</option></tube>
<tube><option value="4">Aldgate East Tube Station</option></tube>
<tube><option value="5">All Saints Tube Station</option></tube>
<tube><option value="6">Alperton Tube Station</option></tube>
<tube><option value="7">Angel Tube Station</option></tube>
<tube><option value="8">Archway Tube Station</option></tube>
<tube><option value="9">Arnos Grove Tube Station</option></tube>
<tube><option value="10">Arsenal Tube Station</option></tube>
<tube><option value="11">Baker Street Tube Station</option></tube>
<tube><option value="12">Balham Tube Station</option></tube>
<tube><option value="13">Bank Tube Station</option></tube>
<tube><option value="14">Barbican Tube Station</option></tube>
<tube><option value="15">Barking Tube Station</option></tube>
<tube><option value="16">Barkingside Tube Station</option></tube>
<tube><option value="17">Barons Court Tube Station</option></tube>
<tube><option value="18">Bayswater Tube Station</option></tube>
<tube><option value="19">Beckton Tube Station</option></tube>
<tube><option value="20">Beckton Park Tube Station</option></tube>
<tube><option value="21">Becontree Tube Station</option></tube>
<tube><option value="22">Belsize Park Tube Station</option></tube>
<tube><option value="23">Bethnal Green Tube Station</option></tube>
<tube><option value="24">Blackfriars Tube Station</option></tube>
<tube><option value="25">Blackhorse Road Tube Station</option></tube>
<tube><option value="26">Blackwall Tube Station</option></tube>
<tube><option value="27">Bond Street Tube Station</option></tube>
<tube><option value="28">Borough Tube Station</option></tube>
<tube><option value="29">Boston Manor Tube Station</option></tube>
<tube><option value="30">Bounds Green Tube Station</option></tube>
<tube><option value="31">Bow Church Tube Station</option></tube>
<tube><option value="32">Bow Road Tube Station</option></tube>
<tube><option value="33">Brent Cross Tube Station</option></tube>
<tube><option value="34">Bromley-By-Bow Tube Station</option></tube>
<tube><option value="35">Burnt Oak Tube Station</option></tube>
<tube><option value="36">Caledonian Road Tube Station</option></tube>
<tube><option value="37">Camden Town Tube Station</option></tube>
<tube><option value="38">Canary Wharf Tube Station</option></tube>
<tube><option value="39">Cannon Street Tube Station</option></tube>
<tube><option value="40">Canons Park Tube Station</option></tube>
<tube><option value="41">Chalk Farm Tube Station</option></tube>
<tube><option value="42">Chancery Lane Tube Station</option></tube>
<tube><option value="43">Charing Cross Tube Station</option></tube>
<tube><option value="44">Chigwell Tube Station</option></tube>
<tube><option value="45">Chiswick Park Tube Station</option></tube>
<tube><option value="46">Clapham Common Tube Station</option></tube>
<tube><option value="47">Clapham North Tube Station</option></tube>
<tube><option value="48">Clapham South Tube Station</option></tube>
<tube><option value="49">Colindale Tube Station</option></tube>
<tube><option value="50">Colliers Wood Tube Station</option></tube>
<tube><option value="51">Covent Garden Tube Station</option></tube>
<tube><option value="52">Crossharbour &amp; London Arena Tube Station</option></tube>
<tube><option value="53">Custom House Tube Station</option></tube>
<tube><option value="54">Cyprus Tube Station</option></tube>
<tube><option value="55">Dagenham East Tube Station</option></tube>
<tube><option value="56">Dagenham Heathway Tube Station</option></tube>
<tube><option value="57">Devons Road Tube Station</option></tube>
<tube><option value="58">Dollis Hill Tube Station</option></tube>
<tube><option value="59">Ealing Broadway Tube Station</option></tube>
<tube><option value="60">Ealing Common Tube Station</option></tube>
<tube><option value="61">Earl's Court Tube Station</option></tube>
<tube><option value="62">Eastcote Tube Station</option></tube>
<tube><option value="63">East Acton Tube Station</option></tube>
<tube><option value="64">East Finchley Tube Station</option></tube>
<tube><option value="65">East Ham Tube Station</option></tube>
<tube><option value="66">East India Tube Station</option></tube>
<tube><option value="67">East Putney Tube Station</option></tube>
<tube><option value="68">Edgware Tube Station</option></tube>
<tube><option value="69">Edgware Road (B) Tube Station</option></tube>
<tube><option value="70">Edgware Road (C) Tube Station</option></tube>
<tube><option value="71">Elephant &amp; Castle Tube Station</option></tube>
<tube><option value="72">Elm Park Tube Station</option></tube>
<tube><option value="73">Embankment Tube Station</option></tube>
<tube><option value="74">Euston Tube Station</option></tube>
<tube><option value="75">Euston Square Tube Station</option></tube>
<tube><option value="76">Fairlop Tube Station</option></tube>
<tube><option value="77">Farringdon Tube Station</option></tube>
<tube><option value="78">Finchley Central Tube Station</option></tube>
<tube><option value="79">Finchley Road Tube Station</option></tube>
<tube><option value="80">Finsbury Park Tube Station</option></tube>
<tube><option value="81">Fulham Broadway Tube Station</option></tube>
<tube><option value="82">Gallions Reach Tube Station</option></tube>
<tube><option value="83">Gants Hill Tube Station</option></tube>
<tube><option value="84">Gloucester Road Tube Station</option></tube>
<tube><option value="85">Golders Green Tube Station</option></tube>
<tube><option value="86">Goldhawk Road Tube Station</option></tube>
<tube><option value="87">Goodge Street Tube Station</option></tube>
<tube><option value="88">Grange Hill Tube Station</option></tube>
<tube><option value="89">Great Portland Street Tube Station</option></tube>
<tube><option value="90">Greenford Tube Station</option></tube>
<tube><option value="91">Green Park Tube Station</option></tube>
<tube><option value="92">Gunnersbury Tube Station</option></tube>
<tube><option value="93">Hainault Tube Station</option></tube>
<tube><option value="94">Hammersmith Tube Station</option></tube>
<tube><option value="95">Hampstead Tube Station</option></tube>
<tube><option value="96">Hanger Lane Tube Station</option></tube>
<tube><option value="97">Harlesden Tube Station</option></tube>
<tube><option value="98">Harrow &amp; Wealdston Tube Station</option></tube>
<tube><option value="99">Harrow-on-the-Hill Tube Station</option></tube>
<tube><option value="100">Hatton Cross Tube Station</option></tube>
<tube><option value="101">Heathrow Terminals 1, 2 &amp; 3 Tube Station</option></tube>
<tube><option value="102">Heathrow Terminal 4 Tube Station</option></tube>
<tube><option value="103">Hendon Central Tube Station</option></tube>
<tube><option value="104">Heron Quays Tube Station</option></tube>
<tube><option value="105">High Street Kensington Tube Station</option></tube>
<tube><option value="106">Highbury &amp; Islington Tube Station</option></tube>
<tube><option value="107">Highgate Tube Station</option></tube>
<tube><option value="108">Hillingdon Tube Station</option></tube>
<tube><option value="109">Holborn Tube Station</option></tube>
<tube><option value="110">Holland Park Tube Station</option></tube>
<tube><option value="111">Holloway Road Tube Station</option></tube>
<tube><option value="112">Hornchurch Tube Station</option></tube>
<tube><option value="113">Hounslow Central Tube Station</option></tube>
<tube><option value="114">Hounslow East Tube Station</option></tube>
<tube><option value="115">Hounslow West Tube Station</option></tube>
<tube><option value="116">Hyde Park Corner Tube Station</option></tube>
<tube><option value="117">Ickenham Tube Station</option></tube>
<tube><option value="118">Island Gardens Tube Station</option></tube>
<tube><option value="119">Kennington Tube Station</option></tube>
<tube><option value="120">Kensal Green Tube Station</option></tube>
<tube><option value="121">Kensington (Olympia) Tube Station</option></tube>
<tube><option value="122">Kentish Town Tube Station</option></tube>
<tube><option value="123">Kenton Tube Station</option></tube>
<tube><option value="124">Kew Gardens Tube Station</option></tube>
<tube><option value="125">Kilburn Tube Station</option></tube>
<tube><option value="126">Kingsbury Tube Station</option></tube>
<tube><option value="127">King's Cross St. Pancras Tube Station</option></tube>
<tube><option value="128">Knightsbridge Tube Station</option></tube>
<tube><option value="129">Ladbroke Grove Tube Station</option></tube>
<tube><option value="130">Lambeth North Tube Station</option></tube>
<tube><option value="131">Lancaster Gate Tube Station</option></tube>
<tube><option value="132">Latimer Road Tube Station</option></tube>
<tube><option value="133">Leicester Square Tube Station</option></tube>
<tube><option value="134">Leyton Tube Station</option></tube>
<tube><option value="135">Leytonstone Tube Station</option></tube>
<tube><option value="136">Limehouse Tube Station</option></tube>
<tube><option value="137">Liverpool Street Tube Station</option></tube>
<tube><option value="138">London Bridge Tube Station</option></tube>
<tube><option value="139">Maida Vale Tube Station</option></tube>
<tube><option value="140">Manor House Tube Station</option></tube>
<tube><option value="141">Mansion House Tube Station</option></tube>
<tube><option value="142">Marble Arch Tube Station</option></tube>
<tube><option value="143">Marylebone Tube Station</option></tube>
<tube><option value="144">Mile End Tube Station</option></tube>
<tube><option value="145">Mill Hill East Tube Station</option></tube>
<tube><option value="146">Monument Tube Station</option></tube>
<tube><option value="147">Moorgate Tube Station</option></tube>
<tube><option value="148">Moor Park Tube Station</option></tube>
<tube><option value="149">Morden Tube Station</option></tube>
<tube><option value="150">Mornington Crescent Tube Station</option></tube>
<tube><option value="151">Mudchute Tube Station</option></tube>
<tube><option value="152">Neasden Tube Station</option></tube>
<tube><option value="153">Newbury Park Tube Station</option></tube>
<tube><option value="154">Northfields Tube Station</option></tube>
<tube><option value="155">Northolt Tube Station</option></tube>
<tube><option value="156">Northwick Park Tube Station</option></tube>
<tube><option value="157">Northwood Tube Station</option></tube>
<tube><option value="158">Northwood Hills Tube Station</option></tube>
<tube><option value="159">North Acton Tube Station</option></tube>
<tube><option value="160">North Ealing Tube Station</option></tube>
<tube><option value="161">North Harrow Tube Station</option></tube>
<tube><option value="162">North Wembley Tube Station</option></tube>
<tube><option value="163">Notting Hill Gate Tube Station</option></tube>
<tube><option value="164">Old Street Tube Station</option></tube>
<tube><option value="165">Osterley Tube Station</option></tube>
<tube><option value="166">Oval Tube Station</option></tube>
<tube><option value="167">Oxford Circus Tube Station</option></tube>
<tube><option value="168">Paddington Tube Station</option></tube>
<tube><option value="169">Park Royal Tube Station</option></tube>
<tube><option value="170">Parsons Green Tube Station</option></tube>
<tube><option value="171">Perivale Tube Station</option></tube>
<tube><option value="172">Picadilly Circus Tube Station</option></tube>
<tube><option value="173">Pimlico Tube Station</option></tube>
<tube><option value="174">Pinner Tube Station</option></tube>
<tube><option value="175">Plaistow Tube Station</option></tube>
<tube><option value="176">Poplar Tube Station</option></tube>
<tube><option value="177">Preston Road Tube Station</option></tube>
<tube><option value="178">Prince Regent Tube Station</option></tube>
<tube><option value="179">Putney Bridge Tube Station</option></tube>
<tube><option value="180">Queen's Park Tube Station</option></tube>
<tube><option value="181">Queensbury Tube Station</option></tube>
<tube><option value="182">Queensway Tube Station</option></tube>
<tube><option value="183">Ravenscourt Park Tube Station</option></tube>
<tube><option value="184">Rayners Lane Tube Station</option></tube>
<tube><option value="185">Redbridge Tube Station</option></tube>
<tube><option value="186">Regent's Park Tube Station</option></tube>
<tube><option value="187">Richmond Tube Station</option></tube>
<tube><option value="188">Roding Valley Tube Station</option></tube>
<tube><option value="189">Rotherhithe Tube Station</option></tube>
<tube><option value="190">Royal Albert Tube Station</option></tube>
<tube><option value="191">Royal Oak Tube Station</option></tube>
<tube><option value="192">Royal Victoria Tube Station</option></tube>
<tube><option value="193">Ruislip Tube Station</option></tube>
<tube><option value="194">Ruislip Manor Tube Station</option></tube>
<tube><option value="195">Russell Square Tube Station</option></tube>
<tube><option value="196">Seven Sisters Tube Station</option></tube>
<tube><option value="197">Shadwell Tube Station</option></tube>
<tube><option value="198">Shepherd's Bush (C) Tube Station</option></tube>
<tube><option value="199">Shepherd's Bush (H) Tube Station</option></tube>
<tube><option value="200">Shoreditch Tube Station</option></tube>
<tube><option value="201">Sloane Square Tube Station</option></tube>
<tube><option value="202">Snaresbrook Tube Station</option></tube>
<tube><option value="203">Southfields Tube Station</option></tube>
<tube><option value="204">South Ealing Tube Station</option></tube>
<tube><option value="205">South Harrow Tube Station</option></tube>
<tube><option value="206">South Kensington Tube Station</option></tube>
<tube><option value="207">South Kenton Tube Station</option></tube>
<tube><option value="208">South Quay Tube Station</option></tube>
<tube><option value="209">South Ruislip Tube Station</option></tube>
<tube><option value="210">South Wimbledon Tube Station</option></tube>
<tube><option value="211">South Woodford Tube Station</option></tube>
<tube><option value="212">Stamford Brook Tube Station</option></tube>
<tube><option value="213">Stanmore Tube Station</option></tube>
<tube><option value="214">Stepney Green Tube Station</option></tube>
<tube><option value="215">Stockwell Tube Station</option></tube>
<tube><option value="216">Stonebridge Park Tube Station</option></tube>
<tube><option value="217">Stratford Tube Station</option></tube>
<tube><option value="218">St. James's Park Tube Station</option></tube>
<tube><option value="219">St. John's Wood Tube Station</option></tube>
<tube><option value="220">St. Paul's Tube Station</option></tube>
<tube><option value="221">Sudbury Hill Tube Station</option></tube>
<tube><option value="222">Sudbury Town Tube Station</option></tube>
<tube><option value="223">Surrey Quays Tube Station</option></tube>
<tube><option value="224">Swiss Cottage Tube Station</option></tube>
<tube><option value="225">Temple Tube Station</option></tube>
<tube><option value="226">Tooting Bec Tube Station</option></tube>
<tube><option value="227">Tooting Broadway Tube Station</option></tube>
<tube><option value="228">Tottenham Court Road Tube Station</option></tube>
<tube><option value="229">Tottenham Hale Tube Station</option></tube>
<tube><option value="230">Tower Gateway Tube Station</option></tube>
<tube><option value="231">Tower Hill Tube Station</option></tube>
<tube><option value="232">Tufnell Park Tube Station</option></tube>
<tube><option value="233">Turnham Green Tube Station</option></tube>
<tube><option value="234">Turnpike Lane Tube Station</option></tube>
<tube><option value="235">Upminster Tube Station</option></tube>
<tube><option value="236">Upminster Bridge Tube Station</option></tube>
<tube><option value="237">Upney Tube Station</option></tube>
<tube><option value="238">Upton Park Tube Station</option></tube>
<tube><option value="239">Uxbridge Tube Station</option></tube>
<tube><option value="240">Vauxhall Tube Station</option></tube>
<tube><option value="241">Victoria Tube Station</option></tube>
<tube><option value="242">Walthamstow Central Tube Station</option></tube>
<tube><option value="243">Wanstead Tube Station</option></tube>
<tube><option value="244">Wapping Tube Station</option></tube>
<tube><option value="245">Warren Street Tube Station</option></tube>
<tube><option value="246">Warwick Avenue Tube Station</option></tube>
<tube><option value="247">Waterloo Tube Station</option></tube>
<tube><option value="248">Wembley Central Tube Station</option></tube>
<tube><option value="249">Wembley Park Tube Station</option></tube>
<tube><option value="250">Westbourne Park Tube Station</option></tube>
<tube><option value="251">Westferry Tube Station</option></tube>
<tube><option value="252">Westminster Tube Station</option></tube>
<tube><option value="253">West Acton Tube Station</option></tube>
<tube><option value="254">West Brompton Tube Station</option></tube>
<tube><option value="255">West Finchley Tube Station</option></tube>
<tube><option value="256">West Ham Tube Station</option></tube>
<tube><option value="257">West Hampstead Tube Station</option></tube>
<tube><option value="258">West Harrow Tube Station</option></tube>
<tube><option value="259">West India Quay Tube Station</option></tube>
<tube><option value="260">West Kensington Tube Station</option></tube>
<tube><option value="261">West Ruislip Tube Station</option></tube>
<tube><option value="262">Whitechapel Tube Station</option></tube>
<tube><option value="263">White City Tube Station</option></tube>
<tube><option value="264">Willesden Green Tube Station</option></tube>
<tube><option value="265">Willesden Junction Tube Station</option></tube>
<tube><option value="266">Wimbledon Tube Station</option></tube>
<tube><option value="267">Wimbledon Park Tube Station</option></tube>
<tube><option value="268">Woodford Tube Station</option></tube>
<tube><option value="269">Woodside Park Tube Station</option></tube>
<tube><option value="270">Wood Green Tube Station</option></tube>
<tube><option value="271">Brixton Tube Station</option></tube>
<tube><option value="272">Amersham Tube Station</option></tube>
<tube><option value="273">Bermondsey Tube Station</option></tube>
<tube><option value="274">Chesham Tube Station</option></tube>
<tube><option value="275">Chalfont &amp; Latimer Tube Station</option></tube>
<tube><option value="276">Chorleywood Tube Station</option></tube>
<tube><option value="277">Rickmansworth Tube Station</option></tube>
<tube><option value="278">Croxley Tube Station</option></tube>
<tube><option value="279">Watford Tube Station</option></tube>
<tube><option value="280">Ruislip Gardens Tube Station</option></tube>
<tube><option value="281">High Barnet Tube Station</option></tube>
<tube><option value="282">Totteridge &amp; Whetstone Tube Station</option></tube>
<tube><option value="283">Cockfosters Tube Station</option></tube>
<tube><option value="284">Oakwood Tube Station</option></tube>
<tube><option value="285">Southgate Tube Station</option></tube>
<tube><option value="286">Epping Tube Station</option></tube>
<tube><option value="287">Theydon Bois Tube Station</option></tube>
<tube><option value="288">Debden Tube Station</option></tube>
<tube><option value="289">Loughton Tube Station</option></tube>
<tube><option value="290">Buckhurst Hill Tube Station</option></tube>
<tube><option value="291">Pudding Mill Lane Tube Station</option></tube>
<tube><option value="292">Southwark Tube Station</option></tube>
<tube><option value="293">Canada Water Tube Station</option></tube>
<tube><option value="294">Canning Town Tube Station</option></tube>
<tube><option value="295">North Greenwich Tube Station</option></tube>
<tube><option value="296">Cutty Sark Tube Station</option></tube>
<tube><option value="297">Greenwich Tube Station</option></tube>
<tube><option value="298">Deptford Bridge Tube Station</option></tube>
<tube><option value="299">Elverson Road Tube Station</option></tube>
<tube><option value="300">Lewisham Tube Station</option></tube>
<tube><option value="301">New Cross Tube Station</option></tube>
<tube><option value="302">New Cross Gate Tube Station</option></tube>
<tube><option value="303">West Silvertown Tube Station</option></tube>
<tube><option value="304">King George V Tube Station</option></tube>
<tube><option value="305">Pontoon Dock Tube Station</option></tube>
<tube><option value="306">London City Airport Tube Station</option></tube>
</tubes>
"""
		hacktree = minidom.parseString(rawresponse)
		nodecount = 0
		idlist = ""
		for node in hacktree.getElementsByTagName('tube'):
			indexname = ""
			nodecount += 1
			tubename = node.getElementsByTagName('option')[0].firstChild.nodeValue
			tubewordlist = tubename.split(" ")
			indexname = "".join(tubewordlist)
			location = models.Location()
			location.name = tubename
			location.location_type = "tubestation"
			location.indexname = indexname.lower()
			location.locationid = models.get_new_locationid()
			location.put()
			#models.increment_count("total_locations")
		template_values = {
						'nodecount': nodecount,
						}
		viewhelpers.render_template(self, "adminviews/dataloader", template_values)
