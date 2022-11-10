class ViewportLocators(object):
    FINAL_RENDER = '//*[local-name() = "path" and @d="M4,4H7L9,2H15L17,4H20A2,2 0 0,1 22,6V18A2,2 0 0,1 20,20H4A2,2 0 0,1 2,18V6A2,2 0 0,1 4,4M12,7A5,5 0 0,0 7,12A5,5 0 0,0 12,17A5,5 0 0,0 17,12A5,5 0 0,0 12,7M12,9A3,3 0 0,1 15,12A3,3 0 0,1 12,15A3,3 0 0,1 9,12A3,3 0 0,1 12,9Z"]'
    SETTING = '(//div[ contains(@class, "app-header-center") ]//div[ contains(@class, "menu-left") ]//button)[1]'
    PROPERTIES = '//button/div[contains(text(), "Properties")]'
    SCENE_INDEX = '//button/div[contains(text(), "Scene Index")]'
    FRIDGE = '//div[contains(text(), "Body")]'
    SCENE_INDEX_TAB = '//./button/div[ text() = "Scene Index" ]'
    SCENE_INDEX_TEXT = '//h3[ text() = "Scene Index" ]'
    SCENE_SEARCH = '//input[ @placeholder="Search Scene" ]'
    PARENT_TREE = '//div[ @id="scene-index-prim-0" ]//div[ @class="py-1" ]'
    TIMELINE_BAR = '//./button/div[ text() = "Timeline" ]'
    TIMELINE_VIEW = '//div[ text() = " Timeline view " ]'
    COMMENTS_BAR = '//./button/div[ text() = "Comments" ]'
    COMMENT = '//div[ text() = " Comment 1" ]'
    SETTINGS_WINDOW = '//div[ contains(@class, "app-header-center") ]//div[ contains(@class, "menu-left") ]//button'
    SETTINGS_TEXT = '//h3[ text() = "Selection viewport" ]'
    SCENE_MENU = '//button[ @class = "button-iconed" ]'
    MENU_ITEM = '//button[ @class = "menu-item" ]'
    VERSIONS_MENU = '//button[ text() = "Versions" ]'
    VERSIONS_WINDOW = '//div[ @class = "card-sectioned-text-container" ]'
    VERSION_SERVICE_NAMES = f'//div[ @class = "font-bold" ]'
    VERSION_ROWS = f'//div[ @class = "version-text" ]'
    
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
    WIDTH = '(//*[@maxlength])[1]'
    HEIGHT = '(//*[@maxlength])[2]'
    BACK_BUTTON ='(//div[@class="icon"])[3]'
    RENDER_SPINNER = '//*[contains(@class,"animate-spin")]'
    WIDTH = '(//*[@maxlength])[1]'
    HEIGHT = '(//*[@maxlength])[2]'
    SAMPLES = '(//*[@maxlength])[3]'
    BACK_BUTTON ='(//div[@class="icon"])[3]'
    DOWNLOAD_IMAGE = '//div[ @class="render-progress-bar-button" ]//button'

class LibraryLocators(object):
    LIBRARY_TAB = '//./button/div[ text() = "Library" ]'
    MATERIALS_TEXT = '//h3[ text() = "Materials" ]'
    SCENE_INDEX_TAB = '//./button/div[ text() = "Scene Index" ]'
    SCENE_SEARCH = '//input[ @placeholder="Search Scene" ]'
    MATERIAL = '//./div[ @class="click-area" ]//h2[ text()=\"'
    SORTING_BY = '/html/body/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[3]/button'
    SORTING_KEY = '/html/body/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div[2]//div//*[ text()=\"'
    MATERIAL_CARD = '//div[ contains(@class, "materials-table-content") ]//h2'
    SEARCH_MATERIAL_CARD = '//div[ @class="material-card" ]//h2'
    SEARCH_MATERIAL = '//input[ @placeholder="Search" ]'

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
