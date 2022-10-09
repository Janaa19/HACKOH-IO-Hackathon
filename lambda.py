import json
import logging
import boto3
import gettext 

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.dispatch_components import(
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractRequestInterceptor)
from ask_sdk_core.utils import is_intent_name, is_request_type

from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

from alexa import data, util

dynamodb = boto3.resource('dynamodb')
response = table.get_item(TableName='AWSHACKOHIO', Key={'info1', info1})


sb = SkillBuilder()

logger = logging.getLogger(_name_)
logger.setLevel(logging.INFO)

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)
    
    def handle(self, handler_input):
        logger.info("In LaunchRequestHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]
        
        data2 = client.get_item()
        
        speech = _(data.WELCOME)
        speech += " " + _(data.HELP)
        handler_input.response_builder.speak(speech)
        handler_input.response_builder.ask(_(data.GENERIC_REPROMPT))
        return handler_input.response_builder.response

class Math_HWHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("Math_HW")(handler_input)
    
    def handle(self, handler_input):
        logger.info("In Math_HWHandler")
        
        attributes_manager = handler_input.attributes_manager
        session_attr = attributes_manager.session_attributes
        
        iterationNum = 0;
        repeatLoop = true;
        while(repeatLoop):
            iterationNum += 1
            information = "info"
            question = "question"
            information += iterationNum
            question += iterationNum
            ask = false
            if iterationNum < 3:
                #speech = Math_HW.(information)
                #speech += " " + Math_HW.(question)
                print("mathhw")
                ask = true
            elif iterationNum < 4:
                #speech = Math_HW.(information)
                print("mathhw2")
            else:
                repeatLoop = false
                
        #mathHW = data.RESPONSE_DATA, "mathHomework"

        #if ask:
            #handler_input.response_builder.speak(speech).ask(speech)
        #else:
            #handler_input.response_builder.speak(speech)
        return handler_input.response_builder.response

class Physics_HWHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("Physics_HW")(handler_input)
    
    def handle(self, handler_input):
        logger.info("In Physics_HWHandler")
        
        attributes_manager = handler_input.attributes_manager
        session_attr = attributes_manager.session_attributes
        
        iterationNum = 0;
        repeatLoop = true;
        while(repeatLoop):
            iterationNum += 1
            information = "info"
            question = "question"
            information += iterationNum
            question += iterationNum
            ask = false
            if iterationNum < 3:
                #speech = Physics_HW.(information)
                #speech += " " + Physics_HW.(question)
                print("physhw")
                ask = true
            elif iterationNum < 4:
                #speech = Physics_HW.(information)
                print("physhw2")
            else:
                repeatLoop = false
                
        #physicsHW = data.RESPONSE_DATA, "physicsHomework"
        
        #if ask:
            #handler_input.response_builder.speak(speech).ask(speech)
        #else:
            #handler_input.response_builder.speak(speech)
        return handler_input.response_builder.response

class Math_TestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("Math_Test")(handler_input)
    
    def handle(self, handler_input):
        logger.info("In Math_TestHandler")
        
        attributes_manager = handler_input.attributes_manager
        session_attr = attributes_manager.session_attributes
        
        iterationNum = 0;
        repeatLoop = true;
        while(repeatLoop):
            iterationNum += 1
            information = "info"
            question = "question"
            information += iterationNum
            question += iterationNum
            ask = false
            if iterationNum < 2:
                #speech = Math_Test.(information)
                #speech += " " + Math_Test.(question)
                print("mathtest")
                ask = true
            elif iterationNum < 3:
                #speech = Math_Test.(information)
                print("mathtest2")
            else:
                repeatLoop = false
                
        #mathTest = data.RESPONSE_DATA, "MathTest"

        #if ask:
            #handler_input.response_builder.speak(speech).ask(speech)
        #else:
            #handler_input.response_builder.speak(speech)
        return handler_input.response_builder.response

class Physics_TestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("Physics_Test")(handler_input)
    
    def handle(self, handler_input):
        logger.info("In Physics_TestHandler")
        
        attributes_manager = handler_input.attributes_manager
        session_attr = attributes_manager.session_attributes
        
        iterationNum = 0;
        repeatLoop = true;
        while(repeatLoop):
            iterationNum += 1
            information = "info"
            question = "question"
            information += iterationNum
            question += iterationNum
            ask = false
            if iterationNum < 3:
                #speech = Physics_Test.(information)
                #speech += " " + Physics_Test.(question)
                print("phystest")
                ask = true
            elif iterationNum < 4:
                #speech = Physics_Test.(information)
                print("phystest")
            else:
                repeatLoop = false
                
        #physicsTest = data.RESPONSE_DATA, "PhysicsTest"

        #if ask:
            #handler_input.response_builder.speak(speech).ask(speech)
        #else:
            #handler_input.response_builder.speak(speech)
        return handler_input.response_builder.response

class Chemistry_TestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("Chemistry_Test")(handler_input)
        
    def handle(self, handler_input):
        logger.info("In Chemistry_TestHandler")
        
        attributes_manager = handler_input.attributes_manager
        session_attr = attributes_manager.session_attributes
        
        iterationNum = 0;
        repeatLoop = true;
        while(repeatLoop):
            iterationNum += 1
            information = "info"
            question = "question"
            information += iterationNum
            question += iterationNum
            ask = false
            if iterationNum < 2:
                #speech = Chemistry_Test.(information)
                #speech += " " + Chemistry_Test.(question)
                print("chemtest")
                ask = true
            elif iterationNum < 3:
                #speech = Chemistry_Test.(information)
                print("chemtest2")
            else:
                repeatLoop = false
                
        #chemistryTest = data.RESPONSE_DATA, "ChemistryTest"

        #if ask:
            #handler_input.response_builder.speak(speech).ask(speech)
        #else:
            #handler_input.response_builder.speak(speech)
        return handler_input.response_builder.response

class Chemistry_HWHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("Chemistry_HW")(handler_input)
    
    def handle(self, handler_input):
        logger.info("In Chemistry_HWHandler")
        
        attributes_manager = handler_input.attributes_manager
        session_attr = attributes_manager.session_attributes
        
        iterationNum = 0;
        repeatLoop = true;
        while(repeatLoop):
            iterationNum += 1
            information = "info"
            question = "question"
            information += iterationNum
            question += iterationNum
            ask = false
            if iterationNum < 2:
                #speech = Chemistry_HW.(information)
                #speech += " " + Chemistry_HW.(information)
                print("chemhw")
                ask = true
            elif iterationNum < 3:
                #speech = Chemistry_HW.(information)
                print("chemhw2")
            else:
                repeatLoop = false
                
        #chemistryHW = data.RESPONSE_DATA, "chemistryHomework"

        #if ask:
            #handler_input.response_builder.speak(speech).ask(speech)
        #else:
            #handler_input.response_builder.speak(speech)
        return handler_input.response_builder.response

class FASFA_Financial_AidHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("FASFA_Financial_Aid")(handler_input)
    
    def handle(self, handler_input):
        logger.info("In FASFA_Financial_AidHandler")
        
        attributes_manager = handler_input.attributes_manager
        session_attr = attributes_manager.session_attributes
        
        iterationNum = 0;
        repeatLoop = true;
        while(repeatLoop):
            iterationNum += 1
            information = "info"
            question = "question"
            information += iterationNum
            question += iterationNum
            ask = false
            if iterationNum < 1:
                #speech = FASFA_Financial_Aid.(information)
                #speech += " " + FASFA_Financial_Aid.(question)
                print("fafsa")
                ask = true
            elif iterationNum < 2:
                #speech = FASFA_Financial_Aid.(information)
                print("fafsa2")
            else:
                repeatLoop = false
                
        #FASFA_Financial_Aid = data.RESPONSE_DATA, "FASFAFinancialAid"

        #if ask:
            #handler_input.response_builder.speak(speech).ask(speech)
        #else:
            #handler_input.response_builder.speak(speech)
        return handler_input.response_builder

class Writing_CenterHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("Writing_Center");
    
    def handle(self, handler_input):
        logger.info("In Writing_Center")
        
        attributes_manager = handler_input.attributes_manager
        session_attr = attributes_manager.session_attributes
        
        iterationNum = 0;
        repeatLoop = true;
        while(repeatLoop):
            iterationNum += 1
            information = "info"
            question = "question"
            information += iterationNum
            question += iterationNum
            ask = false
            if iterationNum < 2:
                #speech = Writing_Center.(information)
                #speech += " " + Writing_Center.(question)
                print("wricenter")
                ask = true
            elif iterationNum < 3:
                #speech = Writing_Center.(information)
                print("wricenter2")
            else:
                repeatLoop = false
                
        #Writing_Center = data.RESPONSE_DATA, "Writing_Center"

        #if ask:
            #handler_input.response_builder.speak(speech).ask(speech)
        #else:
            #handler_input.response_builder.speak(speech)
        return handler_input.response_builder
