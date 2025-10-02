import colorsys

def complementary_color(rgb):
    r, g, b = [x/255.0 for x in rgb]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    h = (h + 0.5) % 1.0
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return (int(r*255), int(g*255), int(b*255))

def recommend_complements(colors):
    return [complementary_color(c) for c in colors]
