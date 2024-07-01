# update_mountains.py
from mountains.models import Mountain

def update_pass_type():
    mountain_pass_types = {
      'Arapahoe Basin Ski Area' : 'ikon', 
      'Aspen Snowmass' : 'ikon',
      'Beaver Creek' : 'epic',
      'Breckenridge' : 'epic',
      'Copper Mountain' : 'ikon',
      'Crested Butte Mountain Resort' : 'epic',
      'Keystone' : 'epic',
      'Loveland Ski Area': 'other',
      'Monarch Mountain': 'other',
      'Powderhorn': 'other',
      'Steamboat': 'ikon',
      'Telluride': 'epic',
      'Vail': 'epic',
      'Winter Park': 'ikon',
      'Wolf Creek Ski Area': 'other',
        # Add more mountain names and their respective pass types
    }
    
    for name, pass_type in mountain_pass_types.items():
        try:
            mountain = Mountain.objects.get(name=name)
            mountain.pass_type = pass_type
            mountain.save()
            print(f"Updated {name} to {pass_type}")
        except Mountain.DoesNotExist:
            print(f"Mountain {name} does not exist in the database.")

if __name__ == "__main__":
    update_pass_type()
