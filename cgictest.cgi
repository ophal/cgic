#!/usr/bin/env luajit

require [[cgic]]

local strlen = string.len
local SERVER_NAME = os.getenv [[SERVER_NAME]]

cgic.init()

function cgiMain()
	-- Load a previously saved CGI scenario if that button has been
  -- pressed.
	if cgic.formSubmitClicked [[loadenvironment]] == cgic.formSuccess then
		LoadEnvironment()
	end
	-- Set any new cookie requested. Must be done *before*
	-- outputting the content type.
	CookieSet()
	-- Send the content type, letting the browser know this is HTML
	cgic.headerContentType [[text/html]]
	-- Top of the page
	--~ print "<HTML><HEAD>\n") TODO: output buffering
	print [[<HTML><HEAD>
<TITLE>cgic test</TITLE></HEAD>
<BODY><H1>cgic test</H1>]]
	-- If a submit button has already been clicked, act on the 
  -- submission of the form.
	if cgic.formSubmitClicked [[testcgic]] == cgic.formSuccess or
		cgic.formSubmitClicked [[saveenvironment]] == cgic.formSuccess then
		HandleSubmit()
		print [[<hr>]]
	end
	-- Now show the form
	ShowForm()
	-- Finish up the page
	print [[</BODY></HTML>]]
	return 0
end

function HandleSubmit()
	Name()
	--~ Address()
	--~ Hungry()
	--~ Temperature()
	--~ Frogs()
	--~ Color()
	--~ Flavors()
	--~ NonExButtons()
	--~ RadioButtons()
	--~ File()
	--~ Entries()
	--~ Cookies()
	-- The saveenvironment button, in addition to submitting the form,
  -- also saves the resulting CGI scenario to disk for later
  -- replay with the 'load saved environment' button.
	if cgic.formSubmitClicked [[saveenvironment]] == cgic.formSuccess then
		SaveEnvironment()
	end
end

function Name()
	local name = ffi.new "char[81]"
	cgic.cgiFormStringNoNewlines(ffi.cast("char *", "name"), name, 81);
	print "Name: "
	cgic.cgiHtmlEscape(name);
	print "<BR>\n"
end
	
--~ void Address() {
	--~ char address[241];
	--~ cgiFormString("address", address, 241);
	--~ fprintf(cgic.cgiOut, "Address: <PRE>\n");
	--~ cgiHtmlEscape(address);
	--~ fprintf(cgic.cgiOut, "</PRE>\n");
--~ }
--~ 
--~ void Hungry() {
	--~ if (cgiFormCheckboxSingle("hungry") == cgiFormSuccess) {
		--~ fprintf(cgic.cgiOut, "I'm Hungry!<BR>\n");
	--~ } else {
		--~ fprintf(cgic.cgiOut, "I'm Not Hungry!<BR>\n");
	--~ }
--~ }
	--~ 
--~ void Temperature() {
	--~ double temperature;
	--~ cgiFormDoubleBounded("temperature", &temperature, 80.0, 120.0, 98.6);
	--~ fprintf(cgic.cgiOut, "My temperature is %f.<BR>\n", temperature);
--~ }
	--~ 
--~ void Frogs() {
	--~ int frogsEaten;
	--~ cgiFormInteger("frogs", &frogsEaten, 0);
	--~ fprintf(cgic.cgiOut, "I have eaten %d frogs.<BR>\n", frogsEaten);
--~ }
--~ 
--~ char *colors[] = {
	--~ "Red",
	--~ "Green",
	--~ "Blue"
--~ };
--~ 
--~ void Color() {
	--~ int colorChoice;
	--~ cgiFormSelectSingle("colors", colors, 3, &colorChoice, 0);
	--~ fprintf(cgic.cgiOut, "I am: %s<BR>\n", colors[colorChoice]);
--~ }	 
--~ 
--~ char *flavors[] = {
	--~ "pistachio",
	--~ "walnut",
	--~ "creme"
--~ };
--~ 
--~ void Flavors() {
	--~ int flavorChoices[3];
	--~ int i;
	--~ int result;	
	--~ int invalid;
	--~ result = cgiFormSelectMultiple("flavors", flavors, 3, 
		--~ flavorChoices, &invalid);
	--~ if (result == cgiFormNotFound) {
		--~ fprintf(cgic.cgiOut, "I hate ice cream.<p>\n");
	--~ } else {	
		--~ fprintf(cgic.cgiOut, "My favorite ice cream flavors are:\n");
		--~ fprintf(cgic.cgiOut, "<ul>\n");
		--~ for (i=0; (i < 3); i++) {
			--~ if (flavorChoices[i]) {
				--~ fprintf(cgic.cgiOut, "<li>%s\n", flavors[i]);
			--~ }
		--~ }
		--~ fprintf(cgic.cgiOut, "</ul>\n");
	--~ }
--~ }
--~ 
--~ char *ages[] = {
	--~ "1",
	--~ "2",
	--~ "3",
	--~ "4"
--~ };
--~ 
--~ void RadioButtons() {
	--~ int ageChoice;
	--~ char ageText[10];
	--~ /* Approach #1: check for one of several valid responses. 
		--~ Good if there are a short list of possible button values and
		--~ you wish to enumerate them. */
	--~ cgiFormRadio("age", ages, 4, &ageChoice, 0);
--~ 
	--~ fprintf(cgic.cgiOut, "Age of Truck: %s (method #1)<BR>\n", 
		--~ ages[ageChoice]);
--~ 
	--~ /* Approach #2: just get the string. Good
		--~ if the information is not critical or if you wish
		--~ to verify it in some other way. Note that if
		--~ the information is numeric, cgiFormInteger,
		--~ cgiFormDouble, and related functions may be
		--~ used instead of cgiFormString. */	
	--~ cgiFormString("age", ageText, 10);
--~ 
	--~ fprintf(cgic.cgiOut, "Age of Truck: %s (method #2)<BR>\n", ageText);
--~ }
--~ 
--~ char *votes[] = {
	--~ "A",
	--~ "B",
	--~ "C",
	--~ "D"
--~ };
--~ 
--~ void NonExButtons() {
	--~ int voteChoices[4];
	--~ int i;
	--~ int result;	
	--~ int invalid;
--~ 
	--~ char **responses;
--~ 
	--~ /* Method #1: check for valid votes. This is a good idea,
		--~ since votes for nonexistent candidates should probably
		--~ be discounted... */
	--~ fprintf(cgic.cgiOut, "Votes (method 1):<BR>\n");
	--~ result = cgiFormCheckboxMultiple("vote", votes, 4, 
		--~ voteChoices, &invalid);
	--~ if (result == cgiFormNotFound) {
		--~ fprintf(cgic.cgiOut, "I hate them all!<p>\n");
	--~ } else {	
		--~ fprintf(cgic.cgiOut, "My preferred candidates are:\n");
		--~ fprintf(cgic.cgiOut, "<ul>\n");
		--~ for (i=0; (i < 4); i++) {
			--~ if (voteChoices[i]) {
				--~ fprintf(cgic.cgiOut, "<li>%s\n", votes[i]);
			--~ }
		--~ }
		--~ fprintf(cgic.cgiOut, "</ul>\n");
	--~ }
--~ 
	--~ /* Method #2: get all the names voted for and trust them.
		--~ This is good if the form will change more often
		--~ than the code and invented responses are not a danger
		--~ or can be checked in some other way. */
	--~ fprintf(cgic.cgiOut, "Votes (method 2):<BR>\n");
	--~ result = cgiFormStringMultiple("vote", &responses);
	--~ if (result == cgiFormNotFound) {	
		--~ fprintf(cgic.cgiOut, "I hate them all!<p>\n");
	--~ } else {
		--~ int i = 0;
		--~ fprintf(cgic.cgiOut, "My preferred candidates are:\n");
		--~ fprintf(cgic.cgiOut, "<ul>\n");
		--~ while (responses[i]) {
			--~ fprintf(cgic.cgiOut, "<li>%s\n", responses[i]);
			--~ i++;
		--~ }
		--~ fprintf(cgic.cgiOut, "</ul>\n");
	--~ }
	--~ /* We must be sure to free the string array or a memory
		--~ leak will occur. Simply calling free() would free
		--~ the array but not the individual strings. The
		--~ function cgiStringArrayFree() does the job completely. */	
	--~ cgiStringArrayFree(responses);
--~ }
--~ 
--~ void Entries()
--~ {
	--~ char **array, **arrayStep;
	--~ fprintf(cgic.cgiOut, "List of All Submitted Form Field Names:<p>\n");
	--~ if (cgiFormEntries(&array) != cgiFormSuccess) {
		--~ return;
	--~ }
	--~ arrayStep = array;
	--~ fprintf(cgic.cgiOut, "<ul>\n");
	--~ while (*arrayStep) {
		--~ fprintf(cgic.cgiOut, "<li>");
		--~ cgiHtmlEscape(*arrayStep);
		--~ fprintf(cgic.cgiOut, "\n");
		--~ arrayStep++;
	--~ }
	--~ fprintf(cgic.cgiOut, "</ul>\n");
	--~ cgiStringArrayFree(array);
--~ }
--~ 
--~ void Cookies()
--~ {
	--~ char **array, **arrayStep;
	--~ char cname[1024], cvalue[1024];
	--~ fprintf(cgic.cgiOut, "Cookies Submitted On This Call, With Values (Many Browsers NEVER Submit Cookies):<p>\n");
	--~ if (cgiCookies(&array) != cgiFormSuccess) {
		--~ return;
	--~ }
	--~ arrayStep = array;
	--~ fprintf(cgic.cgiOut, "<table border=1>\n");
	--~ fprintf(cgic.cgiOut, "<tr><th>Cookie<th>Value</tr>\n");
	--~ while (*arrayStep) {
		--~ char value[1024];
		--~ fprintf(cgic.cgiOut, "<tr>");
		--~ fprintf(cgic.cgiOut, "<td>");
		--~ cgiHtmlEscape(*arrayStep);
		--~ fprintf(cgic.cgiOut, "<td>");
		--~ cgiCookieString(*arrayStep, value, sizeof(value));
		--~ cgiHtmlEscape(value);
		--~ fprintf(cgic.cgiOut, "\n");
		--~ arrayStep++;
	--~ }
	--~ fprintf(cgic.cgiOut, "</table>\n");
	--~ cgiFormString("cname", cname, sizeof(cname));	
	--~ cgiFormString("cvalue", cvalue, sizeof(cvalue));	
	--~ if (strlen(cname)) {
		--~ fprintf(cgic.cgiOut, "New Cookie Set On This Call:<p>\n");
		--~ fprintf(cgic.cgiOut, "Name: ");	
		--~ cgiHtmlEscape(cname);
		--~ fprintf(cgic.cgiOut, "Value: ");	
		--~ cgiHtmlEscape(cvalue);
		--~ fprintf(cgic.cgiOut, "<p>\n");
		--~ fprintf(cgic.cgiOut, "If your browser accepts cookies (many do not), this new cookie should appear in the above list the next time the form is submitted.<p>\n"); 
	--~ }
	--~ cgiStringArrayFree(array);
--~ }
	--~ 
--~ void File()
--~ {
	--~ cgiFilePtr file;
	--~ char name[1024];
	--~ char contentType[1024];
	--~ char buffer[1024];
	--~ int size;
	--~ int got;
	--~ if (cgiFormFileName("file", name, sizeof(name)) != cgiFormSuccess) {
		--~ printf("<p>No file was uploaded.<p>\n");
		--~ return;
	--~ } 
	--~ fprintf(cgic.cgiOut, "The filename submitted was: ");
	--~ cgiHtmlEscape(name);
	--~ fprintf(cgic.cgiOut, "<p>\n");
	--~ cgiFormFileSize("file", &size);
	--~ fprintf(cgic.cgiOut, "The file size was: %d bytes<p>\n", size);
	--~ cgiFormFileContentType("file", contentType, sizeof(contentType));
	--~ fprintf(cgic.cgiOut, "The alleged content type of the file was: ");
	--~ cgiHtmlEscape(contentType);
	--~ fprintf(cgic.cgiOut, "<p>\n");
	--~ fprintf(cgic.cgiOut, "Of course, this is only the claim the browser made when uploading the file. Much like the filename, it cannot be trusted.<p>\n");
	--~ fprintf(cgic.cgiOut, "The file's contents are shown here:<p>\n");
	--~ if (cgiFormFileOpen("file", &file) != cgiFormSuccess) {
		--~ fprintf(cgic.cgiOut, "Could not open the file.<p>\n");
		--~ return;
	--~ }
	--~ fprintf(cgic.cgiOut, "<pre>\n");
	--~ while (cgiFormFileRead(file, buffer, sizeof(buffer), &got) ==
		--~ cgiFormSuccess)
	--~ {
		--~ cgiHtmlEscapeData(buffer, got);
	--~ }
	--~ fprintf(cgic.cgiOut, "</pre>\n");
	--~ cgiFormFileClose(file);
--~ }
--~ 
function ShowForm()
	print(([[<!-- 2.0: multipart/form-data is required for file uploads. -->
<form method="POST" enctype="multipart/form-data" action="%s">]]):format(cgic.scriptName() or [[]]))
print [[<p>
Text Field containing Plaintext
<p>
<input type="text" name="name">Your Name
<p>
Multiple-Line Text Field
<p>
<textarea NAME="address" ROWS=4 COLS=40>
Default contents go here. 
</textarea>
<p>
Checkbox
<p>
<input type="checkbox" name="hungry" checked>Hungry
<p>
Text Field containing a Numeric Value
<p>
<input type="text" name="temperature" value="98.6">
Blood Temperature (80.0-120.0)
<p>
Text Field containing an Integer Value
<p>
<input type="text" name="frogs" value="1">
Frogs Eaten
<p>
Single-SELECT
<br>
<select name="colors">
<option value="Red">Red
<option value="Green">Green
<option value="Blue">Blue
</select>
<br>
Multiple-SELECT
<br>
<select name="flavors" multiple>
<option value="pistachio">Pistachio
<option value="walnut">Walnut
<option value="creme">Creme
</select>
<p>Exclusive Radio Button Group: Age of Truck in Years
<input type="radio" name="age" value="1">1
<input type="radio" name="age" value="2">2
<input type="radio" name="age" value="3" checked>3
<input type="radio" name="age" value="4">4
<p>Nonexclusive Checkbox Group: Voting for Zero through Four Candidates
<input type="checkbox" name="vote" value="A">A
<input type="checkbox" name="vote" value="B">B
<input type="checkbox" name="vote" value="C">C
<input type="checkbox" name="vote" value="D">D
<p>File Upload:
<input type="file" name="file" value=""> (Select A Local File)
<p>
<p>Set a Cookie<p>
<input name="cname" value=""> Cookie Name
<input name="cvalue" value=""> Cookie Value<p>
<input type="submit" name="testcgic" value="Submit Request">
<input type="reset" value="Reset Request">
<p>Save the CGI Environment<p>
Pressing this button will submit the form, then save the CGI environment so that it can be replayed later by calling cgiReadEnvironment (in a debugger, for instance).<p>
<input type="submit" name="saveenvironment" value="Save Environment">
</form>]]
end

function CookieSet()
	-- Must set cookies BEFORE calling cgiHeaderContentType
	local cname = cgic.formString([[cname]], 1024) or [[]]
	local cvalue = cgic.formString([[cvalue]], 1024) or [[]]
	if strlen(cname) > 0 then
		-- Cookie lives for one day (or until browser chooses
		-- to get rid of it, which may be immediately),
    -- and applies only to this script on this site.
		cgic.headerCookieSetString(cname, cvalue,
			86400, cgic.scriptName, SERVER_NAME)
	end
end

function LoadEnvironment()
	if cgic.readEnvironment(SAVED_ENVIRONMENT) ~= cgic.environmentSuccess then
		cgic.headerContentType(ffi.cast([[char *]], [[text/html]]))
		print [[<head>Error</head>
<body><h1>Error</h1>
cgiReadEnvironment failed. Most likely you have not saved an environment yet.]]
		os.exit()
  end
	-- OK, return now and show the results of the saved environment
end

--~ void SaveEnvironment()
--~ {
	--~ if (cgiWriteEnvironment(SAVED_ENVIRONMENT) != 
		--~ cgiEnvironmentSuccess) 
	--~ {
		--~ fprintf(cgic.cgiOut, "<p>cgiWriteEnvironment failed. Most "
			--~ "likely %s is not a valid path or is not "
			--~ "writable by the user that the CGI program "
			--~ "is running as.<p>\n", SAVED_ENVIRONMENT);
	--~ } else {
		--~ fprintf(cgic.cgiOut, "<p>Environment saved. Click this button "
			--~ "to restore it, playing back exactly the same "
			--~ "scenario: "
			--~ "<form method=POST action=\"");
		--~ cgiValueEscape(cgiScriptName);
		--~ fprintf(cgic.cgiOut, "\">" 
			--~ "<input type=\"submit\" "
			--~ "value=\"Load Environment\" "
			--~ "name=\"loadenvironment\"></form><p>\n");
	--~ }
--~ }

cgiMain()
