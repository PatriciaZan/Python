import xml.etree.ElementTree as ET

def load_gpx(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    #print(f"Root Tag:  {root.tag}")

    #for child in root:
        #print(f"Child Tag:  {child.tag}")

    ns = {
        "gpx": "http://www.topografix.com/GPX/1/1",
        "gpxtpx": "http://www.garmin.com/xmlschemas/TrackPointExtension/v1",
    }

    track_points = root.findall(".//gpx:trkpt", ns)

    #print(len(f"Track Points: {track_points}"))


    point = track_points[0]
    #print(f"Point attrib: {point.attrib}")

    elevation = point.find("gpx:ele", ns)
    time = point.find("gpx:time", ns)

    #print(f"Elevation: {elevation.text}")
    #print(f"Time: {time.text}")

    heart_rate = point.find(
        ".//gpxtpx:hr",
        ns
    )

    #print(f"Heart Hate: {heart_rate.text}")

    activity = []

    for point in track_points:
        hr = point.find(".//gpxtpx:hr", ns)

        activity.append({
            "lat": float(point.attrib["lat"]),
            "lon": float(point.attrib["lon"]),
            "elevation": float(point.find("gpx:ele", ns).text),
            "time": point.find("gpx:time", ns).text,
            "heart_rate": int(hr.text) if hr is not None else None,
        })
    print(activity)
    return activity

