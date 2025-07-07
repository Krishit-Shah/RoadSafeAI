# 🚧 Accident Report Fields – Public Form

| Field Name             | Description                                 | Input by Public? | Required? | Remarks                    |
|------------------------|---------------------------------------------|------------------|-----------|----------------------------|
| Latitude               | Location latitude (map click / GPS)         | ✅               | ✅        | Use map input or geocoder |
| Longitude              | Location longitude                          | ✅               | ✅        | Use map input or geocoder |
| Datetime               | Date & Time of accident                     | ✅               | ✅        | Use datetime picker        |
| Police_Force           | Jurisdiction of local police                | ❌               | ❌        | Auto-filled/admin selected |
| Weather_Conditions     | Weather at the time                         | ✅          
     | ✅        | Dropdown (clear, fog, etc) |
| Road_Surface_Conditions| Wet/dry/snow/ice                            | ✅               | ✅        | Dropdown                   |
| Light_Conditions       | Daylight, night, streetlight                | ✅               | ✅        | Dropdown                   |
| Number_of_Vehicles     | Vehicles involved                           | ✅               | ✅        | Numeric                    |
| Number_of_Casualties   | Total injured or dead                       | ✅               | ✅        | Numeric                    |
| Vehicle_Types_Involved | Unique vehicle types                        | ✅               | ✅        | Select multiple (checkbox) |
| Severity_Score         | Risk score based on casualties              | ❌               | ❌        | Calculated automatically   |
