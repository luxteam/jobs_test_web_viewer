class ViewportLocators(object):
    FINAL_RENDER = '//*[local-name() = "path" and @d="M4,4H7L9,2H15L17,4H20A2,2 0 0,1 22,6V18A2,2 0 0,1 20,20H4A2,2 0 0,1 2,18V6A2,2 0 0,1 4,4M12,7A5,5 0 0,0 7,12A5,5 0 0,0 12,17A5,5 0 0,0 17,12A5,5 0 0,0 12,7M12,9A3,3 0 0,1 15,12A3,3 0 0,1 12,15A3,3 0 0,1 9,12A3,3 0 0,1 12,9Z"]'
    PROPERTIES = '//button/div[contains(text(), "Properties")]'
    FRIDGE = '//div[contains(text(), "Body")]'
    SCENE_INDEX_TAB = '//./button/div[ text() = "Scene Index" ]'
    SCENE_INDEX_TEXT = '//h3[ text() = "Scene Index" ]'
    SCENE_SEARCH = '//input[ @placeholder="Search Scene" ]'
    PARENT_TREE = '//div[ @id="scene-index-prim-0" ]//div[ @class="py-1" ]'
    TIMELINE_BAR = '//./button/div[ text() = "Timeline" ]'
    TIMELINE_VIEW = '//div[ text() = " Timeline view " ]'
    COMMENTS_BAR = '//./button/div[ text() = "Comments" ]'
    COMMENT = '//div[ text() = " Comment 1" ]'
    SETTINGS_WINDOW = '//*[local-name() = "path" and @d="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11L21.54,9.37C21.73,9.22 21.78,8.95 21.66,8.73L19.66,5.27C19.54,5.05 19.27,4.96 19.05,5.05L16.56,6.05C16.04,5.66 15.5,5.32 14.87,5.07L14.5,2.42C14.46,2.18 14.25,2 14,2H10C9.75,2 9.54,2.18 9.5,2.42L9.13,5.07C8.5,5.32 7.96,5.66 7.44,6.05L4.95,5.05C4.73,4.96 4.46,5.05 4.34,5.27L2.34,8.73C2.21,8.95 2.27,9.22 2.46,9.37L4.57,11C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.21,15.05 2.34,15.27L4.34,18.73C4.46,18.95 4.73,19.03 4.95,18.95L7.44,17.94C7.96,18.34 8.5,18.68 9.13,18.93L9.5,21.58C9.54,21.82 9.75,22 10,22H14C14.25,22 14.46,21.82 14.5,21.58L14.87,18.93C15.5,18.67 16.04,18.34 16.56,17.94L19.05,18.95C19.27,19.03 19.54,18.95 19.66,18.73L21.66,15.27C21.78,15.05 21.73,14.78 21.54,14.63L19.43,12.97Z"]/..'
    SETTINGS_TEXT = '//h3[ text() = "Selection viewport" ]'
    SCENE_MENU = '//button[ @class = "button-iconed" ]'
    MENU_ITEM = '//button[ @class = "menu-item" ]'
    VERSIONS_MENU = '//button[ text() = "Versions" ]'
    VERSIONS_WINDOW = '//div[ @class = "card-sectioned-text-container" ]'
    VERSION_SERVICE_NAMES = f'//div[ @class = "font-bold" ]'
    VERSION_ROWS = f'//div[ @class = "version-text" ]'
    
    def expand_node(name):
        return '//div[contains(text(), "' + name +'")]/..//div[ contains(@class, "scene-index-prim-button-expand-container") ]'

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
    TIME_TAKEN = '//div[ @class="render-progress-text" ]'

class LibraryLocators(object):
    LIBRARY_TAB = '//./button/div[ text() = "Library" ]'
    MATERIALS_TEXT = '//h3[ text() = "Materials" ]'
    SCENE_INDEX_TAB = '//./button/div[ text() = "Scene Index" ]'
    SCENE_SEARCH = '//input[ @placeholder="Search Scene" ]'
    MATERIAL = '//./div[ @class="click-area" ]//h2[ text()=\"'
    SORTING_BY = '/html/body/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[3]/button'
    SORTING_KEY = '/html/body/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div[2]//div//*[ text()=\"'
    MATERIAL_TITLE = '//div[ contains(@id, "row-0") ]//h2'
    MATERIAL_CARDS = '//div[ starts-with(@id, "row-") ]//div[ contains(@class, "material-card") ]'
    SEARCH_MATERIAL_CARD = '//div[ @class="material-card" ]//h2'
    SEARCH_MATERIAL = '//input[ @placeholder="Search" ]'
    MATERIAL_CARD = '//div[ @class="material-card" ]'

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
