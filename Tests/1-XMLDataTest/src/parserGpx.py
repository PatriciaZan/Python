import gpxpy

# Open and parse the GPX file
with open('./Morning_Ride.gpx', 'r') as gpx_file:
    gpx = gpxpy.parse(gpx_file)

# Loop through tracks, segments, and points
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            print(f"Lat: {point.latitude}, Lon: {point.longitude}, Elev: {point.elevation}, Time: {point.time}")


moving_data = gpx.get_moving_data()
uphill, downhill = gpx.get_uphill_downhill()

print(f"Total distance: {gpx.length_3d()} meters")
print(f"Total ascent: {uphill} meters")
print(f"Moving time: {moving_data.moving_time} seconds")