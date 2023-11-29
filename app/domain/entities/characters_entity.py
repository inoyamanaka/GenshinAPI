class CharacterEntity:
    def __init__(self, name, element, region, img_in_game, img_namecard):
        self.name = name
        self.element = element
        self.region = region
        self.img_in_game = img_in_game
        self.img_namecard = img_namecard
        

class DetailCharacterEntity:
    def __init__(self, name, element, region, img_in_game, img_namecard, skills, constellations, material, recommend_weapon, recommend_artefact):
        self.name = name
        self.element = element
        self.region = region
        self.img_in_game = img_in_game
        self.img_namecard = img_namecard
        self.skills = skills
        self.constellations = constellations
        self.material = material
        self.recommend_weapon = recommend_weapon
        self.recommend_artefact = recommend_artefact