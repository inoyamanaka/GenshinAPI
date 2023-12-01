from weapon_talent_materials_class import WeaponAscensionMaterials
from character_talent_materials_class import CharacterTalentsMaterials

# GENERATE CHARACTER TALENT MATERIALS SCHEDULE

talents_materials_scraper = CharacterTalentsMaterials('https://genshin.gg/farming/')
talents_materials_scraper.scrape_schedule()
talents_materials_scraper.generate_schedule_data()
talents_materials_scraper.save_to_json()

# GENERATE WEAPON ASCENSION MATERIALS SCHEDULE
scraper = WeaponAscensionMaterials('https://genshin.gg/farming/')
scraper.scrape_material_schedule()
scraper.generate_schedule_data()
scraper.save_to_json()