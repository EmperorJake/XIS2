"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from firs import Industry, Tile, Sprite, Spriteset, SpriteLayout, IndustryLayout

"""
Notes to self whilst figuring out python-firs (notes will probably rot here forever).
By convention, ids for use in nml have industry name prefix, local python object ids don't bother with industry name prefix.
Some method properties expect object references, and the templating then uses properties from that object.
Some method properties need a string - the templating is then typically directly writing out an nml identifier.
When a string is expected are basically two choices: provide a string directly, or make an object reference and get an id from that object.
"""

industry = Industry(id='glass_works')

industry.add_tile(id='glass_works_tile')

spriteset_ground = industry.add_spriteset(
    id = 'glass_works_spriteset_ground',
    type='cobble',
)
spriteset_ground_overlay_1 = industry.add_spriteset(
    id = 'glass_works_spriteset_ground_overlay_1',
    sprites = [(10, 10, 64, 31, -31, 0)],
)
spriteset_ground_overlay_2 = industry.add_spriteset(
    id = 'glass_works_spriteset_ground_overlay_2',
    sprites = [(80, 10, 64, 31, -31, 0)],
)
spriteset_ground_overlay_3 = industry.add_spriteset(
    id = 'glass_works_spriteset_ground_overlay_3',
    sprites = [(150, 10, 64, 31, -31, 0)],
)
spriteset_ground_overlay_4 = industry.add_spriteset(
    id = 'glass_works_spriteset_ground_overlay_4',
    sprites = [(220, 10, 64, 31, -31, 0)],
)
spriteset_1 = industry.add_spriteset(
    id = 'glass_works_spriteset_1',
    sprites = [(10, 60, 64, 90, -31, -59)],
    zextent = 12
)
spriteset_2 = industry.add_spriteset(
    id = 'glass_works_spriteset_2',
    sprites = [(80, 60, 64, 90, -31, -71)],
    zextent = 12
)
spriteset_3 = industry.add_spriteset(
    id = 'glass_works_spriteset_3',
    sprites = [(150, 60, 64, 90, -31, -59)],
    zextent = 12
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_small',
    xoffset= 13,
    yoffset= 0,
    zoffset= 54,
)

industry.add_spritelayout(
    id = 'glass_works_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay_1,
    building_sprites = [spriteset_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'glass_works_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay_2,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'glass_works_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay_3,
    building_sprites = [spriteset_3],
    smoke_sprites = [sprite_smoke],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'glass_works_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay_4,
    building_sprites = [],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'glass_works_industry_layout_1',
    default_spritelayout = 'glass_works_spritelayout_4',
    layout = [(0, 0, 'glass_works_tile', 'glass_works_spritelayout_4'),
              (0, 1, 'glass_works_tile', 'glass_works_spritelayout_3'),
              (1, 0, 'glass_works_tile', 'glass_works_spritelayout_1'),
              (1, 1, 'glass_works_tile', 'glass_works_spritelayout_2'),
    ]
)
industry.add_industry_layout(
    id = 'glass_works_industry_layout_2',
    default_spritelayout = 'glass_works_spritelayout_4',
    layout = [(0, 0, 'glass_works_tile', 'glass_works_spritelayout_4'),
              (0, 1, 'glass_works_tile', 'glass_works_spritelayout_3'),
              (1, 0, 'glass_works_tile', 'glass_works_spritelayout_1'),
              (1, 1, 'glass_works_tile', 'glass_works_spritelayout_2'),
              (2, 0, 'glass_works_tile', 'glass_works_spritelayout_4'),
              (2, 1, 'glass_works_tile', 'glass_works_spritelayout_3'),
              (3, 0, 'glass_works_tile', 'glass_works_spritelayout_1'),
              (3, 1, 'glass_works_tile', 'glass_works_spritelayout_2'),
    ]
)
industry.add_industry_layout(
    id = 'glass_works_industry_layout_3',
    default_spritelayout = 'glass_works_spritelayout_4',
    layout = [(0, 0, 'glass_works_tile', 'glass_works_spritelayout_4'),
              (0, 1, 'glass_works_tile', 'glass_works_spritelayout_3'),
              (0, 2, 'glass_works_tile', 'glass_works_spritelayout_4'),
              (0, 3, 'glass_works_tile', 'glass_works_spritelayout_3'),
              (1, 0, 'glass_works_tile', 'glass_works_spritelayout_1'),
              (1, 1, 'glass_works_tile', 'glass_works_spritelayout_2'),
              (1, 2, 'glass_works_tile', 'glass_works_spritelayout_1'),
              (1, 3, 'glass_works_tile', 'glass_works_spritelayout_2'),
              (2, 1, 'glass_works_tile', 'glass_works_spritelayout_4'),
              (2, 2, 'glass_works_tile', 'glass_works_spritelayout_3'),
              (3, 1, 'glass_works_tile', 'glass_works_spritelayout_1'),
              (3, 2, 'glass_works_tile', 'glass_works_spritelayout_2')
    ]
)

# Templating
industry.render_and_save_pnml()