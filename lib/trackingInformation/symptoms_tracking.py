# User logs in securely and goes to symptom page
# on the left their is a drop down list with the heading “Choose a symptom to track“
# Once the arrow is the placeholder text will say “start typyng to search or add your own symptom“
# The list of symptoms that appear will come from an NHS API:
#  if the symptoms is not in there the user can continues to type and button appears below saying “save the sypmtom“ as well as giving a date input to complete (default is todays date but can be put in the past)
#  if the symptoms IS in the list, the user can continue to type and button appears below saying “save the sypmtom“ 
# as well as giving a date input to complete (default is todays date but can be put in the past)
#  - ( the configuration on how the save button comes up in not important)
# once they press “save the symptom“ an input will come up and say - “Add intensity level (optional)“ with a drop down arrow
# the items in the drop down menu will be 1- 10 (1 being low and 10 being extremely severe 
# there will also be a further button that says “save“
# Once “save“ has been pressed:
#  the item will appear in the most recent symptoms tracked area
# the input will be saved along with the intentsity rating (if provided) in the database
# Success: User is able to view their saved item in the “most recent symptoms tracked area“ and the data is available for analysis 