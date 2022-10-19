class ViewportLocators(object):
    FINAL_RENDER = '//*[local-name() = "path" and @d="M4,4H7L9,2H15L17,4H20A2,2 0 0,1 22,6V18A2,2 0 0,1 20,20H4A2,2 0 0,1 2,18V6A2,2 0 0,1 4,4M12,7A5,5 0 0,0 7,12A5,5 0 0,0 12,17A5,5 0 0,0 17,12A5,5 0 0,0 12,7M12,9A3,3 0 0,1 15,12A3,3 0 0,1 12,15A3,3 0 0,1 9,12A3,3 0 0,1 12,9Z"]'
    SCENE_INDEX = '//./button/div[ text() = "Scene Index"]'
    LIBRARY = '//./button/div[ text() = "Library"]'
    PROPERTIES = '//./button/div[ text() = "Properties"]'


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
    MOVE = '//button[contains(., "Move")]'
    MOVE_X = '(//*[contains(@class,"sidebar-container-vertical")]//*[@maxlength])[1]'
    MOVE_Y = '(//*[contains(@class,"sidebar-container-vertical")]//*[@maxlength])[2]'
    MOVE_Z = '(//*[contains(@class,"sidebar-container-vertical")]//*[@maxlength])[3]'

    ROTATE = '//button[contains(., "Rotate")]'
    ROTATE_X = '(//*[contains(@class,"sidebar-container-vertical")]//*[@maxlength])[1]'
    ROTATE_Y = '(//*[contains(@class,"sidebar-container-vertical")]//*[@maxlength])[2]'
    ROTATE_Z = '(//*[contains(@class,"sidebar-container-vertical")]//*[@maxlength])[3]'

    SCALE = '//button[contains(., "Scale")]'
    SCALE_X = '(//*[contains(@class,"sidebar-container-vertical")]//*[@maxlength])[1]'
    SCALE_Y = '(//*[contains(@class,"sidebar-container-vertical")]//*[@maxlength])[2]'
    SCALE_Z = '(//*[contains(@class,"sidebar-container-vertical")]//*[@maxlength])[3]'

class SceneIndexLocators(object):
    SEARCH_SCENE = '//input[ @placeholder="Search Scene"]'

class LibraryLocators(object):
    pass