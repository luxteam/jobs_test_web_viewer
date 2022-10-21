class ViewportLocators(object):
    FINAL_RENDER = '//*[local-name() = "path" and @d="M4,4H7L9,2H15L17,4H20A2,2 0 0,1 22,6V18A2,2 0 0,1 20,20H4A2,2 0 0,1 2,18V6A2,2 0 0,1 4,4M12,7A5,5 0 0,0 7,12A5,5 0 0,0 12,17A5,5 0 0,0 17,12A5,5 0 0,0 12,7M12,9A3,3 0 0,1 15,12A3,3 0 0,1 12,15A3,3 0 0,1 9,12A3,3 0 0,1 12,9Z"]'
    SETTING = '(//div[ contains(@class, "app-header-center") ]//div[ contains(@class, "menu-left") ]//button)[1]'
    PROPERTIES = '//button/div[contains(text(), "Properties")]'
    SCENE_INDEX = '//button/div[contains(text(), "Scene Index")]'
    FRIDGE = '//div[contains(text(), "Body")]'

    def expand_node(name):
        return '//div[contains(text(), "' + name +'")]/..//button[@class=\'scene-index-prim-button-expand\']'

class SettingsLocators(object):
    MOVE_INPUT = '//h4[text()[contains(., "Move")]]/../..//input'
    MOVE_LEFT = '(//h4[text()[contains(., "Move")]]/../..//button)[1]'
    MOVE_RIGHT = '(//h4[text()[contains(., "Move")]]/../..//button)[2]'
    ROTATE_INPUT = '//h4[text()[contains(., "Rotate")]]/../..//input'
    ROTATE_LEFT = '(//h4[text()[contains(., "Rotate")]]/../..//button)[1]'
    ROTATE_RIGHT = '(//h4[text()[contains(., "Rotate")]]/../..//button)[2]'
    SCALE_INPUT = '//h4[text()[contains(., "Scale")]]/../..//input'
    SCALE_LEFT = '(//h4[text()[contains(., "Scale")]]/../..//button)[1]'
    SCALE_RIGHT = '(//h4[text()[contains(., "Scale")]]/../..//button)[2]'

class FinalRenderLocators(object):
    OUTPUT = '//*[text()="Output"]'
    FORMAT = '(//input[@class="containered-input select-text cursor-pointer"])[1]'
    PNG_FORMAT = '(//div[@class="relative"])[1]//button[contains(text(), "PNG")]'
    BEGIN_RENDER = '//div[text()[contains(., "Begin Render")]]'
    RENDER_SPINNER = '//*[contains(@class,"animate-spin")]'
    WIDTH = '(//*[@maxlength])[1]'
    HEIGHT = '(//*[@maxlength])[2]'
    SAMPLES = '(//*[@maxlength])[3]'
    BACK_BUTTON ='(//div[@class="icon"])[3]'

class PropertiesLocators(object):
    MOVE = '//div[@class="expand-button-container"]//h3[text()[contains(., "Move")]]'
    ROTATE = '//div[@class="expand-button-container"]//h3[text()[contains(., "Rotate")]]'
    SCALE = '//div[@class="expand-button-container"]//h3[text()[contains(., "Scale")]]'
    LOCK_BUTTON = '//div[text()[contains(.,"Lock")]]'
    UNLOCK_BUTTON = '//div[text()[contains(.,"Unlock")]]'
    NOT_A_NUMBER_TOOLTIP = '//li[text()[contains(.,"Need to be a number")]]'

    def properties_locators(index, axis):
        if index == "move":
            i = "1"
        elif index == "rotate":
            i = "2"
        elif index == "scale":
            i = "3"
        return ['(//h4[text()[contains(., "' + axis + '")]])[' + i + ']/../..//input', '((//h4[text()[contains(., "' + axis + '")]])[' + i + ']/../..//button)[1]', '((//h4[text()[contains(., "' + axis + '")]])[' + i + ']/../..//button)[2]']
