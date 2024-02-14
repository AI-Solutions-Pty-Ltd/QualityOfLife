<template>
  <div class='row'>

    <div class='col-12 col-sm-12 col-md-10 col-lg-8 col-xl-6 col-xxl-6'>
      <label for="">Search</label>
      <input type="text" v-model="search" class="form-control" placeholder="Search Kanji">
      <template v-if="search" v-for="kanji in kanjis">
        <template v-if="kanji.meaning.includes(search) || kanji.kanji == search">
          <li style="font-size: x-large;">{{ kanji.kanji }} - {{ kanji.meaning }}</li>
        </template>
      </template>
    </div>

    <div class='col-12 col-sm-12 col-md-10 col-lg-8 col-xl-6 col-xxl-6'>
      <button @click="getRandomKanji();" class="btn btn-primary">Get Random Kanji</button>
      <span v-if="random" style="font-size: x-large;">
        {{ random.kanji }}
      </span>
      <button class="btn btn-success" @click="show = true">Show</button>
      <label style="font-size: x-large;" v-if="show">{{ random.meaning }}</label>
    </div>

  </div>
</template>

<script setup>
const kanjis = [
  {
    "kanji": "一",
    "meaning": "one"
  },
  {
    "kanji": "二",
    "meaning": "two"
  },
  {
    "kanji": "三",
    "meaning": "three"
  },
  {
    "kanji": "四",
    "meaning": "four"
  },
  {
    "kanji": "五",
    "meaning": "five"
  },
  {
    "kanji": "六",
    "meaning": "six"
  },
  {
    "kanji": "七",
    "meaning": "seven"
  },
  {
    "kanji": "八",
    "meaning": "eight"
  },
  {
    "kanji": "九",
    "meaning": "nine"
  },
  {
    "kanji": "十",
    "meaning": "ten"
  },
  {
    "kanji": "口",
    "meaning": "mouth"
  },
  {
    "kanji": "日",
    "meaning": "day"
  },
  {
    "kanji": "月",
    "meaning": "month"
  },
  {
    "kanji": "田",
    "meaning": "rice field"
  },
  {
    "kanji": "目",
    "meaning": "eye"
  },
  {
    "kanji": "古",
    "meaning": "old"
  },
  {
    "kanji": "吾",
    "meaning": "I"
  },
  {
    "kanji": "冒",
    "meaning": "risk"
  },
  {
    "kanji": "朋",
    "meaning": "companion"
  },
  {
    "kanji": "明",
    "meaning": "bright"
  },
  {
    "kanji": "唱",
    "meaning": "chant"
  },
  {
    "kanji": "晶",
    "meaning": "sparkle"
  },
  {
    "kanji": "品",
    "meaning": "goods"
  },
  {
    "kanji": "呂",
    "meaning": "spine"
  },
  {
    "kanji": "昌",
    "meaning": "prosperous"
  },
  {
    "kanji": "早",
    "meaning": "early"
  },
  {
    "kanji": "旭",
    "meaning": "rising sun"
  },
  {
    "kanji": "世",
    "meaning": "generation"
  },
  {
    "kanji": "胃",
    "meaning": "stomach"
  },
  {
    "kanji": "旦",
    "meaning": "nightbreak"
  },
  {
    "kanji": "胆",
    "meaning": "gall bladder"
  },
  {
    "kanji": "亘",
    "meaning": "span"
  },
  {
    "kanji": "凹",
    "meaning": "concave"
  },
  {
    "kanji": "凸",
    "meaning": "convex"
  },
  {
    "kanji": "旧",
    "meaning": "olden times"
  },
  {
    "kanji": "自",
    "meaning": "oneself"
  },
  {
    "kanji": "白",
    "meaning": "white"
  },
  {
    "kanji": "百",
    "meaning": "hundred"
  },
  {
    "kanji": "中",
    "meaning": "in"
  },
  {
    "kanji": "千",
    "meaning": "thousand"
  },
  {
    "kanji": "舌",
    "meaning": "tongue"
  },
  {
    "kanji": "升",
    "meaning": "measuring box"
  },
  {
    "kanji": "昇",
    "meaning": "rise up"
  },
  {
    "kanji": "丸",
    "meaning": "round"
  },
  {
    "kanji": "寸",
    "meaning": "measurement"
  },
  {
    "kanji": "専",
    "meaning": "specialty"
  },
  {
    "kanji": "博",
    "meaning": "Dr."
  },
  {
    "kanji": "占",
    "meaning": "fortune-telling"
  },
  {
    "kanji": "上",
    "meaning": "above"
  },
  {
    "kanji": "下",
    "meaning": "below"
  },
  {
    "kanji": "卓",
    "meaning": "eminent"
  },
  {
    "kanji": "朝",
    "meaning": "morning"
  },
  {
    "kanji": "只",
    "meaning": "only"
  },
  {
    "kanji": "貝",
    "meaning": "shellfish"
  },
  {
    "kanji": "貞",
    "meaning": "upright"
  },
  {
    "kanji": "員",
    "meaning": "employee"
  },
  {
    "kanji": "見",
    "meaning": "see"
  },
  {
    "kanji": "児",
    "meaning": "newborn babe"
  },
  {
    "kanji": "元",
    "meaning": "beginning"
  },
  {
    "kanji": "頁",
    "meaning": "page"
  },
  {
    "kanji": "頑",
    "meaning": "stubborn"
  },
  {
    "kanji": "凡",
    "meaning": "mediocre"
  },
  {
    "kanji": "負",
    "meaning": "defeat"
  },
  {
    "kanji": "万",
    "meaning": "ten thousand"
  },
  {
    "kanji": "句",
    "meaning": "phrase"
  },
  {
    "kanji": "肌",
    "meaning": "texture"
  },
  {
    "kanji": "旬",
    "meaning": "decameron"
  },
  {
    "kanji": "勺",
    "meaning": "ladle"
  },
  {
    "kanji": "的",
    "meaning": "bull's eye"
  },
  {
    "kanji": "首",
    "meaning": "neck"
  },
  {
    "kanji": "乙",
    "meaning": "fishguts"
  },
  {
    "kanji": "乱",
    "meaning": "riot"
  },
  {
    "kanji": "直",
    "meaning": "straightaway"
  },
  {
    "kanji": "具",
    "meaning": "tool"
  },
  {
    "kanji": "真",
    "meaning": "TRUE"
  },
  {
    "kanji": "工",
    "meaning": "craft"
  },
  {
    "kanji": "左",
    "meaning": "left"
  },
  {
    "kanji": "右",
    "meaning": "right"
  },
  {
    "kanji": "有",
    "meaning": "possess"
  },
  {
    "kanji": "賄",
    "meaning": "bribe"
  },
  {
    "kanji": "貢",
    "meaning": "tribute"
  },
  {
    "kanji": "項",
    "meaning": "paragraph"
  },
  {
    "kanji": "刀",
    "meaning": "sword"
  },
  {
    "kanji": "刃",
    "meaning": "blade"
  },
  {
    "kanji": "切",
    "meaning": "cut"
  },
  {
    "kanji": "召",
    "meaning": "seduce"
  },
  {
    "kanji": "昭",
    "meaning": "shining"
  },
  {
    "kanji": "則",
    "meaning": "rule"
  },
  {
    "kanji": "副",
    "meaning": "vice-"
  },
  {
    "kanji": "別",
    "meaning": "separate"
  },
  {
    "kanji": "丁",
    "meaning": "street"
  },
  {
    "kanji": "町",
    "meaning": "village"
  },
  {
    "kanji": "可",
    "meaning": "can"
  },
  {
    "kanji": "頂",
    "meaning": "place on the head"
  },
  {
    "kanji": "子",
    "meaning": "child"
  },
  {
    "kanji": "孔",
    "meaning": "cavity"
  },
  {
    "kanji": "了",
    "meaning": "complete"
  },
  {
    "kanji": "女",
    "meaning": "woman"
  },
  {
    "kanji": "好",
    "meaning": "fond"
  },
  {
    "kanji": "如",
    "meaning": "likeness"
  },
  {
    "kanji": "母",
    "meaning": "mama"
  },
  {
    "kanji": "貫",
    "meaning": "pierce"
  },
  {
    "kanji": "兄",
    "meaning": "elder brother"
  },
  {
    "kanji": "克",
    "meaning": "overcome"
  },
  {
    "kanji": "小",
    "meaning": "little"
  },
  {
    "kanji": "少",
    "meaning": "few"
  },
  {
    "kanji": "大",
    "meaning": "large"
  },
  {
    "kanji": "多",
    "meaning": "many"
  },
  {
    "kanji": "夕",
    "meaning": "evening"
  },
  {
    "kanji": "汐",
    "meaning": "eventide"
  },
  {
    "kanji": "外",
    "meaning": "outside"
  },
  {
    "kanji": "名",
    "meaning": "name"
  },
  {
    "kanji": "石",
    "meaning": "stone"
  },
  {
    "kanji": "肖",
    "meaning": "resemblance"
  },
  {
    "kanji": "硝",
    "meaning": "nitrate"
  },
  {
    "kanji": "砕",
    "meaning": "smash"
  },
  {
    "kanji": "砂",
    "meaning": "sand"
  },
  {
    "kanji": "削",
    "meaning": "plane"
  },
  {
    "kanji": "光",
    "meaning": "ray"
  },
  {
    "kanji": "太",
    "meaning": "plump"
  },
  {
    "kanji": "器",
    "meaning": "utensil"
  },
  {
    "kanji": "臭",
    "meaning": "stinking"
  },
  {
    "kanji": "妙",
    "meaning": "exquisite"
  },
  {
    "kanji": "省",
    "meaning": "focus"
  },
  {
    "kanji": "厚",
    "meaning": "thick"
  },
  {
    "kanji": "奇",
    "meaning": "strange"
  },
  {
    "kanji": "川",
    "meaning": "stream"
  },
  {
    "kanji": "州",
    "meaning": "state"
  },
  {
    "kanji": "順",
    "meaning": "obey"
  },
  {
    "kanji": "水",
    "meaning": "water"
  },
  {
    "kanji": "氷",
    "meaning": "icicle"
  },
  {
    "kanji": "永",
    "meaning": "eternity"
  },
  {
    "kanji": "泉",
    "meaning": "spring"
  },
  {
    "kanji": "原",
    "meaning": "meadow"
  },
  {
    "kanji": "願",
    "meaning": "petition"
  },
  {
    "kanji": "泳",
    "meaning": "swim"
  },
  {
    "kanji": "沼",
    "meaning": "marsh"
  },
  {
    "kanji": "沖",
    "meaning": "open sea"
  },
  {
    "kanji": "江",
    "meaning": "creek"
  },
  {
    "kanji": "汁",
    "meaning": "soup"
  },
  {
    "kanji": "潮",
    "meaning": "tide"
  },
  {
    "kanji": "源",
    "meaning": "source"
  },
  {
    "kanji": "活",
    "meaning": "lively"
  },
  {
    "kanji": "消",
    "meaning": "extinguish"
  },
  {
    "kanji": "況",
    "meaning": "but of course"
  },
  {
    "kanji": "河",
    "meaning": "river"
  },
  {
    "kanji": "泊",
    "meaning": "overnight"
  },
  {
    "kanji": "湖",
    "meaning": "lake"
  },
  {
    "kanji": "測",
    "meaning": "fathom"
  },
  {
    "kanji": "土",
    "meaning": "soil"
  },
  {
    "kanji": "吐",
    "meaning": "spit"
  },
  {
    "kanji": "圧",
    "meaning": "pressure"
  },
  {
    "kanji": "埼",
    "meaning": "cape"
  },
  {
    "kanji": "垣",
    "meaning": "hedge"
  },
  {
    "kanji": "圭",
    "meaning": "square jewel"
  },
  {
    "kanji": "封",
    "meaning": "seal"
  },
  {
    "kanji": "涯",
    "meaning": "horizon"
  },
  {
    "kanji": "寺",
    "meaning": "Buddhist temple"
  },
  {
    "kanji": "時",
    "meaning": "time"
  },
  {
    "kanji": "均",
    "meaning": "level"
  },
  {
    "kanji": "火",
    "meaning": "fire"
  },
  {
    "kanji": "炎",
    "meaning": "inflammation"
  },
  {
    "kanji": "煩",
    "meaning": "anxiety"
  },
  {
    "kanji": "淡",
    "meaning": "thin"
  },
  {
    "kanji": "灯",
    "meaning": "lamp"
  },
  {
    "kanji": "畑",
    "meaning": "farm"
  },
  {
    "kanji": "災",
    "meaning": "disaster"
  },
  {
    "kanji": "灰",
    "meaning": "ashes"
  },
  {
    "kanji": "点",
    "meaning": "spot"
  },
  {
    "kanji": "照",
    "meaning": "illuminate"
  },
  {
    "kanji": "魚",
    "meaning": "fish"
  },
  {
    "kanji": "漁",
    "meaning": "fishing"
  },
  {
    "kanji": "里",
    "meaning": "ri"
  },
  {
    "kanji": "黒",
    "meaning": "black"
  },
  {
    "kanji": "墨",
    "meaning": "black ink"
  },
  {
    "kanji": "鯉",
    "meaning": "carp"
  },
  {
    "kanji": "量",
    "meaning": "quantity"
  },
  {
    "kanji": "厘",
    "meaning": "rin"
  },
  {
    "kanji": "埋",
    "meaning": "bury"
  },
  {
    "kanji": "同",
    "meaning": "same"
  },
  {
    "kanji": "洞",
    "meaning": "den"
  },
  {
    "kanji": "胴",
    "meaning": "trunk"
  },
  {
    "kanji": "向",
    "meaning": "yonder"
  },
  {
    "kanji": "尚",
    "meaning": "esteem"
  },
  {
    "kanji": "字",
    "meaning": "character"
  },
  {
    "kanji": "守",
    "meaning": "guard"
  },
  {
    "kanji": "完",
    "meaning": "perfect"
  },
  {
    "kanji": "宣",
    "meaning": "proclaim"
  },
  {
    "kanji": "宵",
    "meaning": "wee hours"
  },
  {
    "kanji": "安",
    "meaning": "relax"
  },
  {
    "kanji": "宴",
    "meaning": "banquet"
  },
  {
    "kanji": "寄",
    "meaning": "draw near"
  },
  {
    "kanji": "富",
    "meaning": "wealth"
  },
  {
    "kanji": "貯",
    "meaning": "savings"
  },
  {
    "kanji": "木",
    "meaning": "tree"
  },
  {
    "kanji": "林",
    "meaning": "grove"
  },
  {
    "kanji": "森",
    "meaning": "forest"
  },
  {
    "kanji": "桂",
    "meaning": "Japanese Judas-tree"
  },
  {
    "kanji": "柏",
    "meaning": "oak"
  },
  {
    "kanji": "枠",
    "meaning": "frame"
  },
  {
    "kanji": "梢",
    "meaning": "treetops"
  },
  {
    "kanji": "棚",
    "meaning": "shelf"
  },
  {
    "kanji": "杏",
    "meaning": "apricot"
  },
  {
    "kanji": "桐",
    "meaning": "paulownia"
  },
  {
    "kanji": "植",
    "meaning": "plant"
  },
  {
    "kanji": "枯",
    "meaning": "wither"
  },
  {
    "kanji": "朴",
    "meaning": "crude"
  },
  {
    "kanji": "村",
    "meaning": "town"
  },
  {
    "kanji": "相",
    "meaning": "inter-"
  },
  {
    "kanji": "机",
    "meaning": "desk"
  },
  {
    "kanji": "本",
    "meaning": "book"
  },
  {
    "kanji": "札",
    "meaning": "tag"
  },
  {
    "kanji": "暦",
    "meaning": "calendar"
  },
  {
    "kanji": "案",
    "meaning": "plan"
  },
  {
    "kanji": "燥",
    "meaning": "parch"
  },
  {
    "kanji": "未",
    "meaning": "not yet"
  },
  {
    "kanji": "末",
    "meaning": "extremity"
  },
  {
    "kanji": "沫",
    "meaning": "splash"
  },
  {
    "kanji": "味",
    "meaning": "flavor"
  },
  {
    "kanji": "妹",
    "meaning": "younger sister"
  },
  {
    "kanji": "朱",
    "meaning": "vermilion"
  },
  {
    "kanji": "株",
    "meaning": "stocks"
  },
  {
    "kanji": "若",
    "meaning": "young"
  },
  {
    "kanji": "草",
    "meaning": "grass"
  },
  {
    "kanji": "苦",
    "meaning": "suffering"
  },
  {
    "kanji": "寛",
    "meaning": "tolerant"
  },
  {
    "kanji": "薄",
    "meaning": "dilute"
  },
  {
    "kanji": "葉",
    "meaning": "leaf"
  },
  {
    "kanji": "模",
    "meaning": "imitation"
  },
  {
    "kanji": "漠",
    "meaning": "vague"
  },
  {
    "kanji": "墓",
    "meaning": "grave"
  },
  {
    "kanji": "暮",
    "meaning": "livelihood"
  },
  {
    "kanji": "膜",
    "meaning": "membrane"
  },
  {
    "kanji": "苗",
    "meaning": "seedling"
  },
  {
    "kanji": "兆",
    "meaning": "portent"
  },
  {
    "kanji": "桃",
    "meaning": "peach tree"
  },
  {
    "kanji": "眺",
    "meaning": "stare"
  },
  {
    "kanji": "犬",
    "meaning": "dog"
  },
  {
    "kanji": "状",
    "meaning": "status quo"
  },
  {
    "kanji": "黙",
    "meaning": "silence"
  },
  {
    "kanji": "然",
    "meaning": "sort of thing"
  },
  {
    "kanji": "荻",
    "meaning": "reed"
  },
  {
    "kanji": "狩",
    "meaning": "hunt"
  },
  {
    "kanji": "猫",
    "meaning": "cat"
  },
  {
    "kanji": "牛",
    "meaning": "cow"
  },
  {
    "kanji": "特",
    "meaning": "special"
  },
  {
    "kanji": "告",
    "meaning": "revelation"
  },
  {
    "kanji": "先",
    "meaning": "before"
  },
  {
    "kanji": "洗",
    "meaning": "wash"
  },
  {
    "kanji": "介",
    "meaning": "jammed in"
  },
  {
    "kanji": "界",
    "meaning": "world"
  },
  {
    "kanji": "茶",
    "meaning": "tea"
  },
  {
    "kanji": "合",
    "meaning": "fit"
  },
  {
    "kanji": "塔",
    "meaning": "pagoda"
  },
  {
    "kanji": "王",
    "meaning": "king"
  },
  {
    "kanji": "玉",
    "meaning": "jewel"
  },
  {
    "kanji": "宝",
    "meaning": "treasure"
  },
  {
    "kanji": "珠",
    "meaning": "pearl"
  },
  {
    "kanji": "現",
    "meaning": "present"
  },
  {
    "kanji": "狂",
    "meaning": "lunatic"
  },
  {
    "kanji": "皇",
    "meaning": "emperor"
  },
  {
    "kanji": "呈",
    "meaning": "display"
  },
  {
    "kanji": "全",
    "meaning": "whole"
  },
  {
    "kanji": "栓",
    "meaning": "plug"
  },
  {
    "kanji": "理",
    "meaning": "logic"
  },
  {
    "kanji": "主",
    "meaning": "lord"
  },
  {
    "kanji": "注",
    "meaning": "pour"
  },
  {
    "kanji": "柱",
    "meaning": "pillar"
  },
  {
    "kanji": "金",
    "meaning": "gold"
  },
  {
    "kanji": "銑",
    "meaning": "pig-iron"
  },
  {
    "kanji": "鉢",
    "meaning": "bowl"
  },
  {
    "kanji": "銅",
    "meaning": "copper"
  },
  {
    "kanji": "釣",
    "meaning": "angling"
  },
  {
    "kanji": "針",
    "meaning": "needle"
  },
  {
    "kanji": "銘",
    "meaning": "inscription"
  },
  {
    "kanji": "鎮",
    "meaning": "tranquilize"
  },
  {
    "kanji": "道",
    "meaning": "road-way"
  },
  {
    "kanji": "導",
    "meaning": "guidance"
  },
  {
    "kanji": "辻",
    "meaning": "crossing"
  },
  {
    "kanji": "迅",
    "meaning": "swift"
  },
  {
    "kanji": "造",
    "meaning": "create"
  },
  {
    "kanji": "迫",
    "meaning": "urge"
  },
  {
    "kanji": "逃",
    "meaning": "escape"
  },
  {
    "kanji": "辺",
    "meaning": "environs"
  },
  {
    "kanji": "巡",
    "meaning": "patrol"
  },
  {
    "kanji": "車",
    "meaning": "car"
  },
  {
    "kanji": "連",
    "meaning": "take along"
  },
  {
    "kanji": "軌",
    "meaning": "rut"
  },
  {
    "kanji": "輸",
    "meaning": "transport"
  },
  {
    "kanji": "前",
    "meaning": "in front"
  },
  {
    "kanji": "各",
    "meaning": "each"
  },
  {
    "kanji": "格",
    "meaning": "status"
  },
  {
    "kanji": "略",
    "meaning": "abbreviation"
  },
  {
    "kanji": "客",
    "meaning": "guest"
  },
  {
    "kanji": "額",
    "meaning": "forehead"
  },
  {
    "kanji": "夏",
    "meaning": "summer"
  },
  {
    "kanji": "処",
    "meaning": "dispose"
  },
  {
    "kanji": "条",
    "meaning": "twig"
  },
  {
    "kanji": "落",
    "meaning": "fall"
  },
  {
    "kanji": "冗",
    "meaning": "superfluous"
  },
  {
    "kanji": "軍",
    "meaning": "army"
  },
  {
    "kanji": "輝",
    "meaning": "radiance"
  },
  {
    "kanji": "運",
    "meaning": "carry"
  },
  {
    "kanji": "冠",
    "meaning": "crown"
  },
  {
    "kanji": "夢",
    "meaning": "dream"
  },
  {
    "kanji": "坑",
    "meaning": "pit"
  },
  {
    "kanji": "高",
    "meaning": "tall"
  },
  {
    "kanji": "享",
    "meaning": "receive"
  },
  {
    "kanji": "塾",
    "meaning": "cram school"
  },
  {
    "kanji": "熟",
    "meaning": "mellow"
  },
  {
    "kanji": "亭",
    "meaning": "pavilion"
  },
  {
    "kanji": "京",
    "meaning": "capital"
  },
  {
    "kanji": "涼",
    "meaning": "refreshing"
  },
  {
    "kanji": "景",
    "meaning": "scenery"
  },
  {
    "kanji": "鯨",
    "meaning": "whale"
  },
  {
    "kanji": "舎",
    "meaning": "cottage"
  },
  {
    "kanji": "周",
    "meaning": "circumference"
  },
  {
    "kanji": "週",
    "meaning": "week"
  },
  {
    "kanji": "士",
    "meaning": "gentleman"
  },
  {
    "kanji": "吉",
    "meaning": "good luck"
  },
  {
    "kanji": "壮",
    "meaning": "robust"
  },
  {
    "kanji": "荘",
    "meaning": "villa"
  },
  {
    "kanji": "売",
    "meaning": "sell"
  },
  {
    "kanji": "学",
    "meaning": "study"
  },
  {
    "kanji": "覚",
    "meaning": "memorize"
  },
  {
    "kanji": "栄",
    "meaning": "flourish"
  },
  {
    "kanji": "書",
    "meaning": "write"
  },
  {
    "kanji": "津",
    "meaning": "haven"
  },
  {
    "kanji": "牧",
    "meaning": "breed"
  },
  {
    "kanji": "攻",
    "meaning": "aggression"
  },
  {
    "kanji": "敗",
    "meaning": "failure"
  },
  {
    "kanji": "枚",
    "meaning": "sheet of..."
  },
  {
    "kanji": "故",
    "meaning": "happenstance"
  },
  {
    "kanji": "敬",
    "meaning": "awe"
  },
  {
    "kanji": "言",
    "meaning": "say"
  },
  {
    "kanji": "警",
    "meaning": "admonish"
  },
  {
    "kanji": "計",
    "meaning": "plot"
  },
  {
    "kanji": "獄",
    "meaning": "prison"
  },
  {
    "kanji": "訂",
    "meaning": "revise"
  },
  {
    "kanji": "討",
    "meaning": "chastise"
  },
  {
    "kanji": "訓",
    "meaning": "instruction"
  },
  {
    "kanji": "詔",
    "meaning": "imperial edict"
  },
  {
    "kanji": "詰",
    "meaning": "packed"
  },
  {
    "kanji": "話",
    "meaning": "tale"
  },
  {
    "kanji": "詠",
    "meaning": "recitation"
  },
  {
    "kanji": "詩",
    "meaning": "poem"
  },
  {
    "kanji": "語",
    "meaning": "word"
  },
  {
    "kanji": "読",
    "meaning": "read"
  },
  {
    "kanji": "調",
    "meaning": "tune"
  },
  {
    "kanji": "談",
    "meaning": "discuss"
  },
  {
    "kanji": "諾",
    "meaning": "consent"
  },
  {
    "kanji": "諭",
    "meaning": "rebuke"
  },
  {
    "kanji": "式",
    "meaning": "style"
  },
  {
    "kanji": "試",
    "meaning": "test"
  },
  {
    "kanji": "弐",
    "meaning": "II"
  },
  {
    "kanji": "域",
    "meaning": "range"
  },
  {
    "kanji": "賊",
    "meaning": "burglar"
  },
  {
    "kanji": "栽",
    "meaning": "plantation"
  },
  {
    "kanji": "載",
    "meaning": "load"
  },
  {
    "kanji": "茂",
    "meaning": "overgrown"
  },
  {
    "kanji": "成",
    "meaning": "turn into"
  },
  {
    "kanji": "城",
    "meaning": "castle"
  },
  {
    "kanji": "誠",
    "meaning": "sincerity"
  },
  {
    "kanji": "威",
    "meaning": "intimidate"
  },
  {
    "kanji": "滅",
    "meaning": "destroy"
  },
  {
    "kanji": "減",
    "meaning": "dwindle"
  },
  {
    "kanji": "桟",
    "meaning": "scaffold"
  },
  {
    "kanji": "銭",
    "meaning": "coin"
  },
  {
    "kanji": "浅",
    "meaning": "shallow"
  },
  {
    "kanji": "止",
    "meaning": "stop"
  },
  {
    "kanji": "歩",
    "meaning": "walk"
  },
  {
    "kanji": "渉",
    "meaning": "ford"
  },
  {
    "kanji": "頻",
    "meaning": "repeatedly"
  },
  {
    "kanji": "肯",
    "meaning": "agreement"
  },
  {
    "kanji": "企",
    "meaning": "undertake"
  },
  {
    "kanji": "歴",
    "meaning": "curriculum"
  },
  {
    "kanji": "武",
    "meaning": "warrior"
  },
  {
    "kanji": "賦",
    "meaning": "levy"
  },
  {
    "kanji": "正",
    "meaning": "correct"
  },
  {
    "kanji": "証",
    "meaning": "evidence"
  },
  {
    "kanji": "政",
    "meaning": "politics"
  },
  {
    "kanji": "定",
    "meaning": "determine"
  },
  {
    "kanji": "錠",
    "meaning": "lock"
  },
  {
    "kanji": "走",
    "meaning": "run"
  },
  {
    "kanji": "超",
    "meaning": "transcend"
  },
  {
    "kanji": "赴",
    "meaning": "proceed"
  },
  {
    "kanji": "越",
    "meaning": "surpass"
  },
  {
    "kanji": "是",
    "meaning": "just so"
  },
  {
    "kanji": "題",
    "meaning": "topic"
  },
  {
    "kanji": "堤",
    "meaning": "dike"
  },
  {
    "kanji": "建",
    "meaning": "build"
  },
  {
    "kanji": "延",
    "meaning": "prolong"
  },
  {
    "kanji": "誕",
    "meaning": "nativity"
  },
  {
    "kanji": "礎",
    "meaning": "cornerstone"
  },
  {
    "kanji": "婿",
    "meaning": "bridegroom"
  },
  {
    "kanji": "衣",
    "meaning": "garment"
  },
  {
    "kanji": "裁",
    "meaning": "tailor"
  },
  {
    "kanji": "装",
    "meaning": "attire"
  },
  {
    "kanji": "裏",
    "meaning": "back"
  },
  {
    "kanji": "壊",
    "meaning": "demolition"
  },
  {
    "kanji": "哀",
    "meaning": "pathetic"
  },
  {
    "kanji": "遠",
    "meaning": "distant"
  },
  {
    "kanji": "猿",
    "meaning": "monkey"
  },
  {
    "kanji": "初",
    "meaning": "first time"
  },
  {
    "kanji": "布",
    "meaning": "linen"
  },
  {
    "kanji": "帆",
    "meaning": "sail"
  },
  {
    "kanji": "幅",
    "meaning": "hanging scroll"
  },
  {
    "kanji": "帽",
    "meaning": "cap"
  },
  {
    "kanji": "幕",
    "meaning": "curtain"
  },
  {
    "kanji": "幌",
    "meaning": "canopy"
  },
  {
    "kanji": "錦",
    "meaning": "brocade"
  },
  {
    "kanji": "市",
    "meaning": "market"
  },
  {
    "kanji": "姉",
    "meaning": "elder sister"
  },
  {
    "kanji": "肺",
    "meaning": "lungs"
  },
  {
    "kanji": "帯",
    "meaning": "sash"
  },
  {
    "kanji": "滞",
    "meaning": "stagnate"
  },
  {
    "kanji": "刺",
    "meaning": "thorn"
  },
  {
    "kanji": "制",
    "meaning": "system"
  },
  {
    "kanji": "製",
    "meaning": "made in..."
  },
  {
    "kanji": "転",
    "meaning": "revolve"
  },
  {
    "kanji": "芸",
    "meaning": "technique"
  },
  {
    "kanji": "雨",
    "meaning": "rain"
  },
  {
    "kanji": "雲",
    "meaning": "cloud"
  },
  {
    "kanji": "曇",
    "meaning": "cloudy weather"
  },
  {
    "kanji": "雷",
    "meaning": "thunder"
  },
  {
    "kanji": "霜",
    "meaning": "frost"
  },
  {
    "kanji": "冬",
    "meaning": "winter"
  },
  {
    "kanji": "天",
    "meaning": "heavens"
  },
  {
    "kanji": "橋",
    "meaning": "bridge"
  },
  {
    "kanji": "嬌",
    "meaning": "attractive"
  },
  {
    "kanji": "立",
    "meaning": "stand up"
  },
  {
    "kanji": "泣",
    "meaning": "cry"
  },
  {
    "kanji": "章",
    "meaning": "badge"
  },
  {
    "kanji": "競",
    "meaning": "vie"
  },
  {
    "kanji": "帝",
    "meaning": "sovereign"
  },
  {
    "kanji": "童",
    "meaning": "juvenile"
  },
  {
    "kanji": "瞳",
    "meaning": "pupil"
  },
  {
    "kanji": "鐘",
    "meaning": "bell"
  },
  {
    "kanji": "商",
    "meaning": "make a deal"
  },
  {
    "kanji": "嫡",
    "meaning": "legitimate wife"
  },
  {
    "kanji": "適",
    "meaning": "suitable"
  },
  {
    "kanji": "滴",
    "meaning": "drip"
  },
  {
    "kanji": "敵",
    "meaning": "enemy"
  },
  {
    "kanji": "匕",
    "meaning": "spoon"
  },
  {
    "kanji": "北",
    "meaning": "north"
  },
  {
    "kanji": "背",
    "meaning": "stature"
  },
  {
    "kanji": "比",
    "meaning": "compare"
  },
  {
    "kanji": "昆",
    "meaning": "descendants"
  },
  {
    "kanji": "皆",
    "meaning": "all"
  },
  {
    "kanji": "混",
    "meaning": "mix"
  },
  {
    "kanji": "渇",
    "meaning": "thirst"
  },
  {
    "kanji": "謁",
    "meaning": "audience"
  },
  {
    "kanji": "褐",
    "meaning": "brown"
  },
  {
    "kanji": "喝",
    "meaning": "hoarse"
  },
  {
    "kanji": "旨",
    "meaning": "delicious"
  },
  {
    "kanji": "脂",
    "meaning": "fat"
  },
  {
    "kanji": "壱",
    "meaning": "I (one)"
  },
  {
    "kanji": "毎",
    "meaning": "every"
  },
  {
    "kanji": "敏",
    "meaning": "cleverness"
  },
  {
    "kanji": "梅",
    "meaning": "plum"
  },
  {
    "kanji": "海",
    "meaning": "sea"
  },
  {
    "kanji": "乞",
    "meaning": "beg"
  },
  {
    "kanji": "乾",
    "meaning": "drought"
  },
  {
    "kanji": "腹",
    "meaning": "abdomen"
  },
  {
    "kanji": "複",
    "meaning": "duplicate"
  },
  {
    "kanji": "欠",
    "meaning": "lack"
  },
  {
    "kanji": "吹",
    "meaning": "blow"
  },
  {
    "kanji": "炊",
    "meaning": "cook"
  },
  {
    "kanji": "歌",
    "meaning": "song"
  },
  {
    "kanji": "軟",
    "meaning": "soft"
  },
  {
    "kanji": "次",
    "meaning": "next"
  },
  {
    "kanji": "茨",
    "meaning": "briar"
  },
  {
    "kanji": "資",
    "meaning": "assets"
  },
  {
    "kanji": "姿",
    "meaning": "figure"
  },
  {
    "kanji": "諮",
    "meaning": "consult with"
  },
  {
    "kanji": "賠",
    "meaning": "compensation"
  },
  {
    "kanji": "培",
    "meaning": "cultivate"
  },
  {
    "kanji": "剖",
    "meaning": "divide"
  },
  {
    "kanji": "音",
    "meaning": "sound"
  },
  {
    "kanji": "暗",
    "meaning": "darkness"
  },
  {
    "kanji": "韻",
    "meaning": "rhyme"
  },
  {
    "kanji": "識",
    "meaning": "discriminating"
  },
  {
    "kanji": "鏡",
    "meaning": "mirror"
  },
  {
    "kanji": "境",
    "meaning": "boundary"
  },
  {
    "kanji": "亡",
    "meaning": "deceased"
  },
  {
    "kanji": "盲",
    "meaning": "blind"
  },
  {
    "kanji": "妄",
    "meaning": "delusion"
  },
  {
    "kanji": "荒",
    "meaning": "laid waste"
  },
  {
    "kanji": "望",
    "meaning": "ambition"
  },
  {
    "kanji": "方",
    "meaning": "direction"
  },
  {
    "kanji": "妨",
    "meaning": "disturb"
  },
  {
    "kanji": "坊",
    "meaning": "boy"
  },
  {
    "kanji": "芳",
    "meaning": "perfume"
  },
  {
    "kanji": "肪",
    "meaning": "obese"
  },
  {
    "kanji": "訪",
    "meaning": "call on"
  },
  {
    "kanji": "放",
    "meaning": "set free"
  },
  {
    "kanji": "激",
    "meaning": "violent"
  },
  {
    "kanji": "脱",
    "meaning": "undress"
  },
  {
    "kanji": "説",
    "meaning": "rumor/explanation"
  },
  {
    "kanji": "鋭",
    "meaning": "pointed"
  },
  {
    "kanji": "曽",
    "meaning": "formerly"
  },
  {
    "kanji": "増",
    "meaning": "increase"
  },
  {
    "kanji": "贈",
    "meaning": "presents"
  },
  {
    "kanji": "東",
    "meaning": "east"
  },
  {
    "kanji": "棟",
    "meaning": "ridgepole"
  },
  {
    "kanji": "凍",
    "meaning": "frozen"
  },
  {
    "kanji": "妊",
    "meaning": "pregnancy"
  },
  {
    "kanji": "廷",
    "meaning": "courts"
  },
  {
    "kanji": "染",
    "meaning": "dye"
  },
  {
    "kanji": "燃",
    "meaning": "burn"
  },
  {
    "kanji": "賓",
    "meaning": "V.I.P."
  },
  {
    "kanji": "歳",
    "meaning": "year-end"
  },
  {
    "kanji": "県",
    "meaning": "prefecture"
  },
  {
    "kanji": "栃",
    "meaning": "horse chestnut"
  },
  {
    "kanji": "地",
    "meaning": "ground"
  },
  {
    "kanji": "池",
    "meaning": "pond"
  },
  {
    "kanji": "虫",
    "meaning": "insect"
  },
  {
    "kanji": "蛍",
    "meaning": "lightning-bug"
  },
  {
    "kanji": "蛇",
    "meaning": "snake"
  },
  {
    "kanji": "虹",
    "meaning": "rainbow"
  },
  {
    "kanji": "蝶",
    "meaning": "butterfly"
  },
  {
    "kanji": "独",
    "meaning": "single"
  },
  {
    "kanji": "蚕",
    "meaning": "silkworm"
  },
  {
    "kanji": "風",
    "meaning": "wind"
  },
  {
    "kanji": "己",
    "meaning": "self"
  },
  {
    "kanji": "起",
    "meaning": "rouse"
  },
  {
    "kanji": "妃",
    "meaning": "queen"
  },
  {
    "kanji": "改",
    "meaning": "reformation"
  },
  {
    "kanji": "記",
    "meaning": "scribe"
  },
  {
    "kanji": "包",
    "meaning": "wrap"
  },
  {
    "kanji": "胞",
    "meaning": "placenta"
  },
  {
    "kanji": "砲",
    "meaning": "cannon"
  },
  {
    "kanji": "泡",
    "meaning": "bubbles"
  },
  {
    "kanji": "亀",
    "meaning": "tortoise"
  },
  {
    "kanji": "電",
    "meaning": "electricity"
  },
  {
    "kanji": "竜",
    "meaning": "dragon"
  },
  {
    "kanji": "滝",
    "meaning": "waterfall"
  },
  {
    "kanji": "豚",
    "meaning": "pork"
  },
  {
    "kanji": "逐",
    "meaning": "pursue"
  },
  {
    "kanji": "遂",
    "meaning": "consummate"
  },
  {
    "kanji": "家",
    "meaning": "house"
  },
  {
    "kanji": "嫁",
    "meaning": "marry into"
  },
  {
    "kanji": "豪",
    "meaning": "overpowering"
  },
  {
    "kanji": "腸",
    "meaning": "intestines"
  },
  {
    "kanji": "場",
    "meaning": "location"
  },
  {
    "kanji": "湯",
    "meaning": "hot water"
  },
  {
    "kanji": "羊",
    "meaning": "sheep"
  },
  {
    "kanji": "美",
    "meaning": "beauty"
  },
  {
    "kanji": "洋",
    "meaning": "ocean"
  },
  {
    "kanji": "詳",
    "meaning": "detailed"
  },
  {
    "kanji": "鮮",
    "meaning": "fresh"
  },
  {
    "kanji": "達",
    "meaning": "accomplished"
  },
  {
    "kanji": "羨",
    "meaning": "envious"
  },
  {
    "kanji": "差",
    "meaning": "distinction"
  },
  {
    "kanji": "着",
    "meaning": "don"
  },
  {
    "kanji": "唯",
    "meaning": "solely"
  },
  {
    "kanji": "焦",
    "meaning": "char"
  },
  {
    "kanji": "礁",
    "meaning": "reef"
  },
  {
    "kanji": "集",
    "meaning": "gather"
  },
  {
    "kanji": "准",
    "meaning": "quasi-"
  },
  {
    "kanji": "進",
    "meaning": "advance"
  },
  {
    "kanji": "雑",
    "meaning": "miscellaneous"
  },
  {
    "kanji": "雌",
    "meaning": "feminine/female"
  },
  {
    "kanji": "準",
    "meaning": "semi-"
  },
  {
    "kanji": "奮",
    "meaning": "stirred up"
  },
  {
    "kanji": "奪",
    "meaning": "rob"
  },
  {
    "kanji": "確",
    "meaning": "assurance"
  },
  {
    "kanji": "午",
    "meaning": "noon"
  },
  {
    "kanji": "許",
    "meaning": "permit"
  },
  {
    "kanji": "歓",
    "meaning": "delight"
  },
  {
    "kanji": "権",
    "meaning": "authority"
  },
  {
    "kanji": "観",
    "meaning": "outlook"
  },
  {
    "kanji": "羽",
    "meaning": "feathers"
  },
  {
    "kanji": "習",
    "meaning": "learn"
  },
  {
    "kanji": "翌",
    "meaning": "the following"
  },
  {
    "kanji": "曜",
    "meaning": "weekday"
  },
  {
    "kanji": "濯",
    "meaning": "laundry"
  },
  {
    "kanji": "曰",
    "meaning": "sayeth"
  },
  {
    "kanji": "困",
    "meaning": "quandary"
  },
  {
    "kanji": "固",
    "meaning": "harden"
  },
  {
    "kanji": "国",
    "meaning": "country"
  },
  {
    "kanji": "団",
    "meaning": "group"
  },
  {
    "kanji": "因",
    "meaning": "cause"
  },
  {
    "kanji": "姻",
    "meaning": "matrimony"
  },
  {
    "kanji": "園",
    "meaning": "park"
  },
  {
    "kanji": "回",
    "meaning": "#NAME?"
  },
  {
    "kanji": "壇",
    "meaning": "podium"
  },
  {
    "kanji": "店",
    "meaning": "store"
  },
  {
    "kanji": "庫",
    "meaning": "warehouse"
  },
  {
    "kanji": "庭",
    "meaning": "courtyard"
  },
  {
    "kanji": "庁",
    "meaning": "government office"
  },
  {
    "kanji": "床",
    "meaning": "bed"
  },
  {
    "kanji": "麻",
    "meaning": "hemp"
  },
  {
    "kanji": "磨",
    "meaning": "grind"
  },
  {
    "kanji": "心",
    "meaning": "heart"
  },
  {
    "kanji": "忘",
    "meaning": "forget"
  },
  {
    "kanji": "忍",
    "meaning": "endure"
  },
  {
    "kanji": "認",
    "meaning": "acknowledge"
  },
  {
    "kanji": "忌",
    "meaning": "mourning"
  },
  {
    "kanji": "志",
    "meaning": "intention"
  },
  {
    "kanji": "誌",
    "meaning": "document"
  },
  {
    "kanji": "忠",
    "meaning": "loyalty"
  },
  {
    "kanji": "串",
    "meaning": "shish kebab"
  },
  {
    "kanji": "患",
    "meaning": "afflicted"
  },
  {
    "kanji": "思",
    "meaning": "think"
  },
  {
    "kanji": "恩",
    "meaning": "grace"
  },
  {
    "kanji": "応",
    "meaning": "apply"
  },
  {
    "kanji": "意",
    "meaning": "idea"
  },
  {
    "kanji": "想",
    "meaning": "concept"
  },
  {
    "kanji": "息",
    "meaning": "breath"
  },
  {
    "kanji": "憩",
    "meaning": "recess"
  },
  {
    "kanji": "恵",
    "meaning": "favor"
  },
  {
    "kanji": "恐",
    "meaning": "fear"
  },
  {
    "kanji": "惑",
    "meaning": "beguile"
  },
  {
    "kanji": "感",
    "meaning": "emotion"
  },
  {
    "kanji": "憂",
    "meaning": "melancholy"
  },
  {
    "kanji": "寡",
    "meaning": "widow"
  },
  {
    "kanji": "忙",
    "meaning": "busy"
  },
  {
    "kanji": "悦",
    "meaning": "ecstasy"
  },
  {
    "kanji": "恒",
    "meaning": "constancy"
  },
  {
    "kanji": "悼",
    "meaning": "lament"
  },
  {
    "kanji": "悟",
    "meaning": "enlightenment"
  },
  {
    "kanji": "怖",
    "meaning": "dreadful"
  },
  {
    "kanji": "慌",
    "meaning": "disconcerted"
  },
  {
    "kanji": "悔",
    "meaning": "repent"
  },
  {
    "kanji": "憎",
    "meaning": "hate"
  },
  {
    "kanji": "慣",
    "meaning": "accustomed"
  },
  {
    "kanji": "愉",
    "meaning": "pleasure"
  },
  {
    "kanji": "惰",
    "meaning": "lazy"
  },
  {
    "kanji": "慎",
    "meaning": "humility"
  },
  {
    "kanji": "憾",
    "meaning": "remorse"
  },
  {
    "kanji": "憶",
    "meaning": "recollection"
  },
  {
    "kanji": "慕",
    "meaning": "pining"
  },
  {
    "kanji": "添",
    "meaning": "annexed"
  },
  {
    "kanji": "必",
    "meaning": "invariably"
  },
  {
    "kanji": "泌",
    "meaning": "ooze"
  },
  {
    "kanji": "手",
    "meaning": "hand"
  },
  {
    "kanji": "看",
    "meaning": "watch over"
  },
  {
    "kanji": "摩",
    "meaning": "chafe"
  },
  {
    "kanji": "我",
    "meaning": "ego"
  },
  {
    "kanji": "義",
    "meaning": "righteousness"
  },
  {
    "kanji": "議",
    "meaning": "deliberation"
  },
  {
    "kanji": "犠",
    "meaning": "sacrifice"
  },
  {
    "kanji": "抹",
    "meaning": "rub"
  },
  {
    "kanji": "抱",
    "meaning": "embrace"
  },
  {
    "kanji": "搭",
    "meaning": "board"
  },
  {
    "kanji": "抄",
    "meaning": "extract"
  },
  {
    "kanji": "抗",
    "meaning": "confront"
  },
  {
    "kanji": "批",
    "meaning": "criticism"
  },
  {
    "kanji": "招",
    "meaning": "beckon"
  },
  {
    "kanji": "拓",
    "meaning": "clear (the land)"
  },
  {
    "kanji": "拍",
    "meaning": "clap"
  },
  {
    "kanji": "打",
    "meaning": "strike"
  },
  {
    "kanji": "拘",
    "meaning": "arrest"
  },
  {
    "kanji": "捨",
    "meaning": "discard"
  },
  {
    "kanji": "拐",
    "meaning": "kidnap"
  },
  {
    "kanji": "摘",
    "meaning": "pinch"
  },
  {
    "kanji": "挑",
    "meaning": "challenge"
  },
  {
    "kanji": "指",
    "meaning": "finger"
  },
  {
    "kanji": "持",
    "meaning": "hold"
  },
  {
    "kanji": "括",
    "meaning": "fasten"
  },
  {
    "kanji": "揮",
    "meaning": "brandish"
  },
  {
    "kanji": "推",
    "meaning": "conjecture"
  },
  {
    "kanji": "揚",
    "meaning": "hoist"
  },
  {
    "kanji": "提",
    "meaning": "propose"
  },
  {
    "kanji": "損",
    "meaning": "damage"
  },
  {
    "kanji": "拾",
    "meaning": "pick up"
  },
  {
    "kanji": "担",
    "meaning": "shouldering"
  },
  {
    "kanji": "拠",
    "meaning": "foothold"
  },
  {
    "kanji": "描",
    "meaning": "sketch"
  },
  {
    "kanji": "操",
    "meaning": "maneuver"
  },
  {
    "kanji": "接",
    "meaning": "touch"
  },
  {
    "kanji": "掲",
    "meaning": "put up (a notice)"
  },
  {
    "kanji": "掛",
    "meaning": "hang"
  },
  {
    "kanji": "研",
    "meaning": "polish"
  },
  {
    "kanji": "戒",
    "meaning": "commandment"
  },
  {
    "kanji": "械",
    "meaning": "contraption"
  },
  {
    "kanji": "鼻",
    "meaning": "nose"
  },
  {
    "kanji": "刑",
    "meaning": "punish"
  },
  {
    "kanji": "型",
    "meaning": "mould"
  },
  {
    "kanji": "才",
    "meaning": "genius"
  },
  {
    "kanji": "財",
    "meaning": "property"
  },
  {
    "kanji": "材",
    "meaning": "lumber"
  },
  {
    "kanji": "存",
    "meaning": "suppose"
  },
  {
    "kanji": "在",
    "meaning": "exist"
  },
  {
    "kanji": "乃",
    "meaning": "from"
  },
  {
    "kanji": "携",
    "meaning": "portable"
  },
  {
    "kanji": "及",
    "meaning": "reach out"
  },
  {
    "kanji": "吸",
    "meaning": "suck"
  },
  {
    "kanji": "扱",
    "meaning": "handle"
  },
  {
    "kanji": "丈",
    "meaning": "length"
  },
  {
    "kanji": "史",
    "meaning": "history"
  },
  {
    "kanji": "吏",
    "meaning": "officer"
  },
  {
    "kanji": "更",
    "meaning": "grow late"
  },
  {
    "kanji": "硬",
    "meaning": "stiff"
  },
  {
    "kanji": "又",
    "meaning": "or again"
  },
  {
    "kanji": "双",
    "meaning": "pair"
  },
  {
    "kanji": "桑",
    "meaning": "mulberry"
  },
  {
    "kanji": "隻",
    "meaning": "vessels"
  },
  {
    "kanji": "護",
    "meaning": "safeguard"
  },
  {
    "kanji": "獲",
    "meaning": "seize"
  },
  {
    "kanji": "奴",
    "meaning": "guy"
  },
  {
    "kanji": "怒",
    "meaning": "angry"
  },
  {
    "kanji": "友",
    "meaning": "friend"
  },
  {
    "kanji": "抜",
    "meaning": "slip out"
  },
  {
    "kanji": "投",
    "meaning": "throw"
  },
  {
    "kanji": "没",
    "meaning": "drown"
  },
  {
    "kanji": "設",
    "meaning": "establishment"
  },
  {
    "kanji": "撃",
    "meaning": "beat"
  },
  {
    "kanji": "殻",
    "meaning": "husk"
  },
  {
    "kanji": "支",
    "meaning": "branch"
  },
  {
    "kanji": "技",
    "meaning": "skill"
  },
  {
    "kanji": "枝",
    "meaning": "bough"
  },
  {
    "kanji": "肢",
    "meaning": "limb"
  },
  {
    "kanji": "茎",
    "meaning": "stalk"
  },
  {
    "kanji": "怪",
    "meaning": "suspicious"
  },
  {
    "kanji": "軽",
    "meaning": "lightly"
  },
  {
    "kanji": "叔",
    "meaning": "uncle"
  },
  {
    "kanji": "督",
    "meaning": "coach"
  },
  {
    "kanji": "寂",
    "meaning": "loneliness"
  },
  {
    "kanji": "淑",
    "meaning": "graceful"
  },
  {
    "kanji": "反",
    "meaning": "anti-"
  },
  {
    "kanji": "坂",
    "meaning": "slope"
  },
  {
    "kanji": "板",
    "meaning": "plank"
  },
  {
    "kanji": "返",
    "meaning": "return"
  },
  {
    "kanji": "販",
    "meaning": "marketing"
  },
  {
    "kanji": "爪",
    "meaning": "claw"
  },
  {
    "kanji": "妥",
    "meaning": "gentle"
  },
  {
    "kanji": "乳",
    "meaning": "milk"
  },
  {
    "kanji": "浮",
    "meaning": "floating"
  },
  {
    "kanji": "将",
    "meaning": "leader"
  },
  {
    "kanji": "奨",
    "meaning": "exhort"
  },
  {
    "kanji": "採",
    "meaning": "pick"
  },
  {
    "kanji": "菜",
    "meaning": "vegetable"
  },
  {
    "kanji": "受",
    "meaning": "accept"
  },
  {
    "kanji": "授",
    "meaning": "impart"
  },
  {
    "kanji": "愛",
    "meaning": "love"
  },
  {
    "kanji": "払",
    "meaning": "pay"
  },
  {
    "kanji": "広",
    "meaning": "wide"
  },
  {
    "kanji": "拡",
    "meaning": "broaden"
  },
  {
    "kanji": "鉱",
    "meaning": "mineral"
  },
  {
    "kanji": "弁",
    "meaning": "valve"
  },
  {
    "kanji": "雄",
    "meaning": "masculine/male"
  },
  {
    "kanji": "台",
    "meaning": "pedestal"
  },
  {
    "kanji": "怠",
    "meaning": "neglect"
  },
  {
    "kanji": "治",
    "meaning": "reign"
  },
  {
    "kanji": "始",
    "meaning": "commence"
  },
  {
    "kanji": "胎",
    "meaning": "womb"
  },
  {
    "kanji": "窓",
    "meaning": "window"
  },
  {
    "kanji": "去",
    "meaning": "gone"
  },
  {
    "kanji": "法",
    "meaning": "method"
  },
  {
    "kanji": "会",
    "meaning": "meeting"
  },
  {
    "kanji": "至",
    "meaning": "climax"
  },
  {
    "kanji": "室",
    "meaning": "room"
  },
  {
    "kanji": "到",
    "meaning": "arrival"
  },
  {
    "kanji": "致",
    "meaning": "doth"
  },
  {
    "kanji": "互",
    "meaning": "mutually"
  },
  {
    "kanji": "棄",
    "meaning": "abandon"
  },
  {
    "kanji": "育",
    "meaning": "bring up"
  },
  {
    "kanji": "撤",
    "meaning": "remove"
  },
  {
    "kanji": "充",
    "meaning": "allot"
  },
  {
    "kanji": "銃",
    "meaning": "gun"
  },
  {
    "kanji": "硫",
    "meaning": "sulphur"
  },
  {
    "kanji": "流",
    "meaning": "current"
  },
  {
    "kanji": "允",
    "meaning": "license"
  },
  {
    "kanji": "唆",
    "meaning": "tempt"
  },
  {
    "kanji": "出",
    "meaning": "exit"
  },
  {
    "kanji": "山",
    "meaning": "mountain"
  },
  {
    "kanji": "拙",
    "meaning": "bungling"
  },
  {
    "kanji": "岩",
    "meaning": "boulder"
  },
  {
    "kanji": "炭",
    "meaning": "charcoal"
  },
  {
    "kanji": "岐",
    "meaning": "branch off"
  },
  {
    "kanji": "峠",
    "meaning": "mountain peak/mountain pass"
  },
  {
    "kanji": "崩",
    "meaning": "crumble"
  },
  {
    "kanji": "密",
    "meaning": "secrecy"
  },
  {
    "kanji": "蜜",
    "meaning": "honey"
  },
  {
    "kanji": "嵐",
    "meaning": "storm"
  },
  {
    "kanji": "崎",
    "meaning": "promontory"
  },
  {
    "kanji": "入",
    "meaning": "enter"
  },
  {
    "kanji": "込",
    "meaning": "crowded"
  },
  {
    "kanji": "分",
    "meaning": "part"
  },
  {
    "kanji": "貧",
    "meaning": "poverty"
  },
  {
    "kanji": "頒",
    "meaning": "partition"
  },
  {
    "kanji": "公",
    "meaning": "public"
  },
  {
    "kanji": "松",
    "meaning": "pine tree"
  },
  {
    "kanji": "翁",
    "meaning": "venerable old man"
  },
  {
    "kanji": "訟",
    "meaning": "sue"
  },
  {
    "kanji": "谷",
    "meaning": "valley"
  },
  {
    "kanji": "浴",
    "meaning": "bathe"
  },
  {
    "kanji": "容",
    "meaning": "contain"
  },
  {
    "kanji": "溶",
    "meaning": "melt"
  },
  {
    "kanji": "欲",
    "meaning": "longing"
  },
  {
    "kanji": "裕",
    "meaning": "abundant"
  },
  {
    "kanji": "鉛",
    "meaning": "lead (metal)"
  },
  {
    "kanji": "沿",
    "meaning": "run alongside"
  },
  {
    "kanji": "賞",
    "meaning": "prize"
  },
  {
    "kanji": "党",
    "meaning": "party"
  },
  {
    "kanji": "堂",
    "meaning": "public chamber/hall"
  },
  {
    "kanji": "常",
    "meaning": "usual"
  },
  {
    "kanji": "裳",
    "meaning": "skirt"
  },
  {
    "kanji": "掌",
    "meaning": "manipulate"
  },
  {
    "kanji": "皮",
    "meaning": "pelt"
  },
  {
    "kanji": "波",
    "meaning": "waves"
  },
  {
    "kanji": "婆",
    "meaning": "old woman"
  },
  {
    "kanji": "披",
    "meaning": "expose"
  },
  {
    "kanji": "破",
    "meaning": "rend"
  },
  {
    "kanji": "被",
    "meaning": "incur"
  },
  {
    "kanji": "残",
    "meaning": "remainder"
  },
  {
    "kanji": "殉",
    "meaning": "martyrdom"
  },
  {
    "kanji": "殊",
    "meaning": "particularly"
  },
  {
    "kanji": "殖",
    "meaning": "augment"
  },
  {
    "kanji": "列",
    "meaning": "file"
  },
  {
    "kanji": "裂",
    "meaning": "split"
  },
  {
    "kanji": "烈",
    "meaning": "ardent"
  },
  {
    "kanji": "死",
    "meaning": "death"
  },
  {
    "kanji": "葬",
    "meaning": "interment"
  },
  {
    "kanji": "瞬",
    "meaning": "wink"
  },
  {
    "kanji": "耳",
    "meaning": "ear"
  },
  {
    "kanji": "取",
    "meaning": "take"
  },
  {
    "kanji": "趣",
    "meaning": "gist"
  },
  {
    "kanji": "最",
    "meaning": "utmost"
  },
  {
    "kanji": "撮",
    "meaning": "snapshot"
  },
  {
    "kanji": "恥",
    "meaning": "shame"
  },
  {
    "kanji": "職",
    "meaning": "post"
  },
  {
    "kanji": "聖",
    "meaning": "holy"
  },
  {
    "kanji": "敢",
    "meaning": "daring"
  },
  {
    "kanji": "聴",
    "meaning": "listen"
  },
  {
    "kanji": "懐",
    "meaning": "pocket"
  },
  {
    "kanji": "慢",
    "meaning": "ridicule"
  },
  {
    "kanji": "漫",
    "meaning": "loose"
  },
  {
    "kanji": "買",
    "meaning": "buy"
  },
  {
    "kanji": "置",
    "meaning": "placement"
  },
  {
    "kanji": "罰",
    "meaning": "penalty"
  },
  {
    "kanji": "寧",
    "meaning": "rather"
  },
  {
    "kanji": "濁",
    "meaning": "voiced"
  },
  {
    "kanji": "環",
    "meaning": "ring"
  },
  {
    "kanji": "還",
    "meaning": "send back"
  },
  {
    "kanji": "夫",
    "meaning": "husband"
  },
  {
    "kanji": "扶",
    "meaning": "aid"
  },
  {
    "kanji": "渓",
    "meaning": "mountain stream"
  },
  {
    "kanji": "規",
    "meaning": "standard"
  },
  {
    "kanji": "替",
    "meaning": "exchange"
  },
  {
    "kanji": "賛",
    "meaning": "approve"
  },
  {
    "kanji": "潜",
    "meaning": "submerge"
  },
  {
    "kanji": "失",
    "meaning": "lose"
  },
  {
    "kanji": "鉄",
    "meaning": "iron"
  },
  {
    "kanji": "迭",
    "meaning": "transfer/alternate"
  },
  {
    "kanji": "臣",
    "meaning": "retainer"
  },
  {
    "kanji": "姫",
    "meaning": "princess"
  },
  {
    "kanji": "蔵",
    "meaning": "storehouse"
  },
  {
    "kanji": "臓",
    "meaning": "entrails"
  },
  {
    "kanji": "賢",
    "meaning": "intelligent"
  },
  {
    "kanji": "堅",
    "meaning": "strict"
  },
  {
    "kanji": "臨",
    "meaning": "look to"
  },
  {
    "kanji": "覧",
    "meaning": "perusal"
  },
  {
    "kanji": "巨",
    "meaning": "gigantic"
  },
  {
    "kanji": "拒",
    "meaning": "repel"
  },
  {
    "kanji": "力",
    "meaning": "power"
  },
  {
    "kanji": "男",
    "meaning": "male/man"
  },
  {
    "kanji": "労",
    "meaning": "labor"
  },
  {
    "kanji": "募",
    "meaning": "recruit"
  },
  {
    "kanji": "劣",
    "meaning": "inferiority"
  },
  {
    "kanji": "功",
    "meaning": "achievement"
  },
  {
    "kanji": "勧",
    "meaning": "persuade"
  },
  {
    "kanji": "努",
    "meaning": "toil"
  },
  {
    "kanji": "励",
    "meaning": "encourage"
  },
  {
    "kanji": "加",
    "meaning": "add"
  },
  {
    "kanji": "賀",
    "meaning": "congratulations"
  },
  {
    "kanji": "架",
    "meaning": "erect"
  },
  {
    "kanji": "脇",
    "meaning": "armpit"
  },
  {
    "kanji": "脅",
    "meaning": "threaten"
  },
  {
    "kanji": "協",
    "meaning": "co-"
  },
  {
    "kanji": "行",
    "meaning": "going"
  },
  {
    "kanji": "律",
    "meaning": "rhythm"
  },
  {
    "kanji": "復",
    "meaning": "restore"
  },
  {
    "kanji": "得",
    "meaning": "gain"
  },
  {
    "kanji": "従",
    "meaning": "accompany"
  },
  {
    "kanji": "徒",
    "meaning": "junior"
  },
  {
    "kanji": "待",
    "meaning": "wait"
  },
  {
    "kanji": "往",
    "meaning": "journey"
  },
  {
    "kanji": "征",
    "meaning": "subjugate"
  },
  {
    "kanji": "径",
    "meaning": "diameter"
  },
  {
    "kanji": "彼",
    "meaning": "he"
  },
  {
    "kanji": "役",
    "meaning": "duty"
  },
  {
    "kanji": "徳",
    "meaning": "benevolence"
  },
  {
    "kanji": "徹",
    "meaning": "penetrate"
  },
  {
    "kanji": "徴",
    "meaning": "indications"
  },
  {
    "kanji": "懲",
    "meaning": "penal"
  },
  {
    "kanji": "微",
    "meaning": "delicate"
  },
  {
    "kanji": "街",
    "meaning": "boulevard"
  },
  {
    "kanji": "衡",
    "meaning": "equilibrium"
  },
  {
    "kanji": "稿",
    "meaning": "draft"
  },
  {
    "kanji": "稼",
    "meaning": "earnings"
  },
  {
    "kanji": "程",
    "meaning": "extent"
  },
  {
    "kanji": "税",
    "meaning": "tax"
  },
  {
    "kanji": "稚",
    "meaning": "immature"
  },
  {
    "kanji": "和",
    "meaning": "harmony"
  },
  {
    "kanji": "移",
    "meaning": "shift"
  },
  {
    "kanji": "秒",
    "meaning": "second"
  },
  {
    "kanji": "秋",
    "meaning": "autumn"
  },
  {
    "kanji": "愁",
    "meaning": "distress"
  },
  {
    "kanji": "私",
    "meaning": "private"
  },
  {
    "kanji": "秩",
    "meaning": "regularity"
  },
  {
    "kanji": "秘",
    "meaning": "secret"
  },
  {
    "kanji": "称",
    "meaning": "appellation"
  },
  {
    "kanji": "利",
    "meaning": "profit"
  },
  {
    "kanji": "梨",
    "meaning": "pear tree"
  },
  {
    "kanji": "穫",
    "meaning": "harvest"
  },
  {
    "kanji": "穂",
    "meaning": "ear (of a plant)"
  },
  {
    "kanji": "稲",
    "meaning": "rice plant"
  },
  {
    "kanji": "香",
    "meaning": "incense"
  },
  {
    "kanji": "季",
    "meaning": "seasons"
  },
  {
    "kanji": "委",
    "meaning": "committee"
  },
  {
    "kanji": "秀",
    "meaning": "excel"
  },
  {
    "kanji": "透",
    "meaning": "transparent"
  },
  {
    "kanji": "誘",
    "meaning": "entice"
  },
  {
    "kanji": "穀",
    "meaning": "cereals"
  },
  {
    "kanji": "菌",
    "meaning": "germ"
  },
  {
    "kanji": "米",
    "meaning": "rice"
  },
  {
    "kanji": "粉",
    "meaning": "flour"
  },
  {
    "kanji": "粘",
    "meaning": "sticky"
  },
  {
    "kanji": "粒",
    "meaning": "grains"
  },
  {
    "kanji": "粧",
    "meaning": "cosmetics"
  },
  {
    "kanji": "迷",
    "meaning": "astray"
  },
  {
    "kanji": "粋",
    "meaning": "chic"
  },
  {
    "kanji": "糧",
    "meaning": "provisions"
  },
  {
    "kanji": "菊",
    "meaning": "chrysanthemum"
  },
  {
    "kanji": "奥",
    "meaning": "core"
  },
  {
    "kanji": "数",
    "meaning": "number"
  },
  {
    "kanji": "楼",
    "meaning": "watchtower"
  },
  {
    "kanji": "類",
    "meaning": "sort"
  },
  {
    "kanji": "漆",
    "meaning": "lacquer"
  },
  {
    "kanji": "様",
    "meaning": "Esq."
  },
  {
    "kanji": "求",
    "meaning": "request"
  },
  {
    "kanji": "球",
    "meaning": "ball"
  },
  {
    "kanji": "救",
    "meaning": "salvation"
  },
  {
    "kanji": "竹",
    "meaning": "bamboo"
  },
  {
    "kanji": "笑",
    "meaning": "laugh"
  },
  {
    "kanji": "笠",
    "meaning": "bamboo hat"
  },
  {
    "kanji": "笹",
    "meaning": "bamboo grass"
  },
  {
    "kanji": "筋",
    "meaning": "muscle"
  },
  {
    "kanji": "箱",
    "meaning": "box"
  },
  {
    "kanji": "筆",
    "meaning": "writing brush"
  },
  {
    "kanji": "筒",
    "meaning": "cylinder"
  },
  {
    "kanji": "等",
    "meaning": "etc."
  },
  {
    "kanji": "算",
    "meaning": "calculate"
  },
  {
    "kanji": "答",
    "meaning": "solution"
  },
  {
    "kanji": "策",
    "meaning": "scheme"
  },
  {
    "kanji": "簿",
    "meaning": "register"
  },
  {
    "kanji": "築",
    "meaning": "fabricate"
  },
  {
    "kanji": "人",
    "meaning": "person"
  },
  {
    "kanji": "佐",
    "meaning": "assistant"
  },
  {
    "kanji": "但",
    "meaning": "however"
  },
  {
    "kanji": "住",
    "meaning": "dwell"
  },
  {
    "kanji": "位",
    "meaning": "rank"
  },
  {
    "kanji": "仲",
    "meaning": "go-between"
  },
  {
    "kanji": "体",
    "meaning": "body"
  },
  {
    "kanji": "悠",
    "meaning": "permanence/remote"
  },
  {
    "kanji": "件",
    "meaning": "affair"
  },
  {
    "kanji": "仕",
    "meaning": "attend"
  },
  {
    "kanji": "他",
    "meaning": "other"
  },
  {
    "kanji": "伏",
    "meaning": "prostrated"
  },
  {
    "kanji": "伝",
    "meaning": "transmit"
  },
  {
    "kanji": "仏",
    "meaning": "Buddha"
  },
  {
    "kanji": "休",
    "meaning": "rest"
  },
  {
    "kanji": "仮",
    "meaning": "sham/provisional"
  },
  {
    "kanji": "伯",
    "meaning": "chief"
  },
  {
    "kanji": "俗",
    "meaning": "vulgar"
  },
  {
    "kanji": "信",
    "meaning": "faith"
  },
  {
    "kanji": "佳",
    "meaning": "excellent"
  },
  {
    "kanji": "依",
    "meaning": "reliant"
  },
  {
    "kanji": "例",
    "meaning": "example"
  },
  {
    "kanji": "個",
    "meaning": "individual"
  },
  {
    "kanji": "健",
    "meaning": "healthy"
  },
  {
    "kanji": "側",
    "meaning": "side"
  },
  {
    "kanji": "侍",
    "meaning": "waiter"
  },
  {
    "kanji": "停",
    "meaning": "halt"
  },
  {
    "kanji": "値",
    "meaning": "price"
  },
  {
    "kanji": "倣",
    "meaning": "emulate"
  },
  {
    "kanji": "倒",
    "meaning": "overthrow"
  },
  {
    "kanji": "偵",
    "meaning": "spy"
  },
  {
    "kanji": "僧",
    "meaning": "Buddhist priest"
  },
  {
    "kanji": "億",
    "meaning": "hundred million"
  },
  {
    "kanji": "儀",
    "meaning": "ceremony"
  },
  {
    "kanji": "償",
    "meaning": "reparation"
  },
  {
    "kanji": "仙",
    "meaning": "hermit"
  },
  {
    "kanji": "催",
    "meaning": "sponsor"
  },
  {
    "kanji": "仁",
    "meaning": "humanity"
  },
  {
    "kanji": "侮",
    "meaning": "scorn"
  },
  {
    "kanji": "使",
    "meaning": "use"
  },
  {
    "kanji": "便",
    "meaning": "convenience"
  },
  {
    "kanji": "倍",
    "meaning": "double"
  },
  {
    "kanji": "優",
    "meaning": "tenderness"
  },
  {
    "kanji": "伐",
    "meaning": "fell"
  },
  {
    "kanji": "宿",
    "meaning": "inn"
  },
  {
    "kanji": "傷",
    "meaning": "wound"
  },
  {
    "kanji": "保",
    "meaning": "protect"
  },
  {
    "kanji": "褒",
    "meaning": "praise"
  },
  {
    "kanji": "傑",
    "meaning": "greatness"
  },
  {
    "kanji": "付",
    "meaning": "adhere"
  },
  {
    "kanji": "符",
    "meaning": "token"
  },
  {
    "kanji": "府",
    "meaning": "borough/municipality"
  },
  {
    "kanji": "任",
    "meaning": "responsibility"
  },
  {
    "kanji": "賃",
    "meaning": "fare"
  },
  {
    "kanji": "代",
    "meaning": "substitute"
  },
  {
    "kanji": "袋",
    "meaning": "sack"
  },
  {
    "kanji": "貸",
    "meaning": "lend"
  },
  {
    "kanji": "化",
    "meaning": "change"
  },
  {
    "kanji": "花",
    "meaning": "flower"
  },
  {
    "kanji": "貨",
    "meaning": "freight"
  },
  {
    "kanji": "傾",
    "meaning": "lean"
  },
  {
    "kanji": "何",
    "meaning": "what"
  },
  {
    "kanji": "荷",
    "meaning": "baggage"
  },
  {
    "kanji": "俊",
    "meaning": "sagacious"
  },
  {
    "kanji": "傍",
    "meaning": "bystander"
  },
  {
    "kanji": "久",
    "meaning": "long time"
  },
  {
    "kanji": "畝",
    "meaning": "furrow"
  },
  {
    "kanji": "囚",
    "meaning": "captured"
  },
  {
    "kanji": "内",
    "meaning": "inside"
  },
  {
    "kanji": "丙",
    "meaning": "third class"
  },
  {
    "kanji": "柄",
    "meaning": "design"
  },
  {
    "kanji": "肉",
    "meaning": "meat"
  },
  {
    "kanji": "腐",
    "meaning": "rot"
  },
  {
    "kanji": "座",
    "meaning": "squat/sit"
  },
  {
    "kanji": "卒",
    "meaning": "graduate"
  },
  {
    "kanji": "傘",
    "meaning": "umbrella"
  },
  {
    "kanji": "匁",
    "meaning": "monme"
  },
  {
    "kanji": "以",
    "meaning": "by means of"
  },
  {
    "kanji": "似",
    "meaning": "becoming/similar"
  },
  {
    "kanji": "併",
    "meaning": "join"
  },
  {
    "kanji": "瓦",
    "meaning": "tile"
  },
  {
    "kanji": "瓶",
    "meaning": "flower pot"
  },
  {
    "kanji": "宮",
    "meaning": "Shinto shrine"
  },
  {
    "kanji": "営",
    "meaning": "occupation"
  },
  {
    "kanji": "善",
    "meaning": "virtuous"
  },
  {
    "kanji": "年",
    "meaning": "year"
  },
  {
    "kanji": "夜",
    "meaning": "night"
  },
  {
    "kanji": "液",
    "meaning": "fluid"
  },
  {
    "kanji": "塚",
    "meaning": "hillock"
  },
  {
    "kanji": "幣",
    "meaning": "cash"
  },
  {
    "kanji": "弊",
    "meaning": "abuse"
  },
  {
    "kanji": "喚",
    "meaning": "yell"
  },
  {
    "kanji": "換",
    "meaning": "interchange"
  },
  {
    "kanji": "融",
    "meaning": "dissolve"
  },
  {
    "kanji": "施",
    "meaning": "alms"
  },
  {
    "kanji": "旋",
    "meaning": "rotation"
  },
  {
    "kanji": "遊",
    "meaning": "play"
  },
  {
    "kanji": "旅",
    "meaning": "trip"
  },
  {
    "kanji": "勿",
    "meaning": "not"
  },
  {
    "kanji": "物",
    "meaning": "thing"
  },
  {
    "kanji": "易",
    "meaning": "easy"
  },
  {
    "kanji": "賜",
    "meaning": "grant"
  },
  {
    "kanji": "尿",
    "meaning": "urine"
  },
  {
    "kanji": "尼",
    "meaning": "nun"
  },
  {
    "kanji": "泥",
    "meaning": "mud"
  },
  {
    "kanji": "塀",
    "meaning": "fence"
  },
  {
    "kanji": "履",
    "meaning": "footgear"
  },
  {
    "kanji": "屋",
    "meaning": "roof"
  },
  {
    "kanji": "握",
    "meaning": "grip"
  },
  {
    "kanji": "屈",
    "meaning": "yield"
  },
  {
    "kanji": "掘",
    "meaning": "dig"
  },
  {
    "kanji": "堀",
    "meaning": "ditch"
  },
  {
    "kanji": "居",
    "meaning": "reside"
  },
  {
    "kanji": "据",
    "meaning": "set"
  },
  {
    "kanji": "層",
    "meaning": "stratum"
  },
  {
    "kanji": "局",
    "meaning": "bureau"
  },
  {
    "kanji": "遅",
    "meaning": "slow"
  },
  {
    "kanji": "漏",
    "meaning": "leak"
  },
  {
    "kanji": "刷",
    "meaning": "printing"
  },
  {
    "kanji": "尺",
    "meaning": "shaku"
  },
  {
    "kanji": "尽",
    "meaning": "exhaust"
  },
  {
    "kanji": "沢",
    "meaning": "swamp"
  },
  {
    "kanji": "訳",
    "meaning": "translate"
  },
  {
    "kanji": "択",
    "meaning": "choose"
  },
  {
    "kanji": "昼",
    "meaning": "daytime"
  },
  {
    "kanji": "戸",
    "meaning": "door"
  },
  {
    "kanji": "肩",
    "meaning": "shoulder"
  },
  {
    "kanji": "房",
    "meaning": "tassel"
  },
  {
    "kanji": "扇",
    "meaning": "fan"
  },
  {
    "kanji": "炉",
    "meaning": "hearth"
  },
  {
    "kanji": "戻",
    "meaning": "re-"
  },
  {
    "kanji": "涙",
    "meaning": "tears"
  },
  {
    "kanji": "雇",
    "meaning": "employ"
  },
  {
    "kanji": "顧",
    "meaning": "look back"
  },
  {
    "kanji": "啓",
    "meaning": "disclose"
  },
  {
    "kanji": "示",
    "meaning": "show"
  },
  {
    "kanji": "礼",
    "meaning": "salute/salutation"
  },
  {
    "kanji": "祥",
    "meaning": "auspicious"
  },
  {
    "kanji": "祝",
    "meaning": "celebrate"
  },
  {
    "kanji": "福",
    "meaning": "blessing"
  },
  {
    "kanji": "祉",
    "meaning": "welfare"
  },
  {
    "kanji": "社",
    "meaning": "company"
  },
  {
    "kanji": "視",
    "meaning": "inspection"
  },
  {
    "kanji": "奈",
    "meaning": "Nara"
  },
  {
    "kanji": "尉",
    "meaning": "military officer"
  },
  {
    "kanji": "慰",
    "meaning": "consolation"
  },
  {
    "kanji": "款",
    "meaning": "goodwill"
  },
  {
    "kanji": "禁",
    "meaning": "prohibition"
  },
  {
    "kanji": "襟",
    "meaning": "collar"
  },
  {
    "kanji": "宗",
    "meaning": "religion"
  },
  {
    "kanji": "崇",
    "meaning": "adore"
  },
  {
    "kanji": "祭",
    "meaning": "ritual"
  },
  {
    "kanji": "察",
    "meaning": "guess"
  },
  {
    "kanji": "擦",
    "meaning": "grate"
  },
  {
    "kanji": "由",
    "meaning": "wherefore"
  },
  {
    "kanji": "抽",
    "meaning": "pluck"
  },
  {
    "kanji": "油",
    "meaning": "oil"
  },
  {
    "kanji": "袖",
    "meaning": "sleeve"
  },
  {
    "kanji": "宙",
    "meaning": "mid-air"
  },
  {
    "kanji": "届",
    "meaning": "deliver"
  },
  {
    "kanji": "笛",
    "meaning": "flute"
  },
  {
    "kanji": "軸",
    "meaning": "axis"
  },
  {
    "kanji": "甲",
    "meaning": "armor"
  },
  {
    "kanji": "押",
    "meaning": "push"
  },
  {
    "kanji": "岬",
    "meaning": "headland"
  },
  {
    "kanji": "挿",
    "meaning": "insert"
  },
  {
    "kanji": "申",
    "meaning": "speaketh"
  },
  {
    "kanji": "伸",
    "meaning": "expand"
  },
  {
    "kanji": "神",
    "meaning": "gods"
  },
  {
    "kanji": "捜",
    "meaning": "search"
  },
  {
    "kanji": "果",
    "meaning": "fruit"
  },
  {
    "kanji": "菓",
    "meaning": "candy/confectionary"
  },
  {
    "kanji": "課",
    "meaning": "chapter"
  },
  {
    "kanji": "裸",
    "meaning": "naked"
  },
  {
    "kanji": "斤",
    "meaning": "axe"
  },
  {
    "kanji": "析",
    "meaning": "chop"
  },
  {
    "kanji": "所",
    "meaning": "place"
  },
  {
    "kanji": "祈",
    "meaning": "pray"
  },
  {
    "kanji": "近",
    "meaning": "near"
  },
  {
    "kanji": "折",
    "meaning": "fold"
  },
  {
    "kanji": "哲",
    "meaning": "philosophy"
  },
  {
    "kanji": "逝",
    "meaning": "departed"
  },
  {
    "kanji": "誓",
    "meaning": "vow"
  },
  {
    "kanji": "暫",
    "meaning": "temporarily"
  },
  {
    "kanji": "漸",
    "meaning": "steadily"
  },
  {
    "kanji": "断",
    "meaning": "severance"
  },
  {
    "kanji": "質",
    "meaning": "substance"
  },
  {
    "kanji": "斥",
    "meaning": "reject"
  },
  {
    "kanji": "訴",
    "meaning": "accusation"
  },
  {
    "kanji": "昨",
    "meaning": "yesterday"
  },
  {
    "kanji": "詐",
    "meaning": "lie"
  },
  {
    "kanji": "作",
    "meaning": "make"
  },
  {
    "kanji": "雪",
    "meaning": "snow"
  },
  {
    "kanji": "録",
    "meaning": "record"
  },
  {
    "kanji": "尋",
    "meaning": "inquire"
  },
  {
    "kanji": "急",
    "meaning": "hurry"
  },
  {
    "kanji": "穏",
    "meaning": "calm"
  },
  {
    "kanji": "侵",
    "meaning": "encroach"
  },
  {
    "kanji": "浸",
    "meaning": "immersed"
  },
  {
    "kanji": "寝",
    "meaning": "lie down"
  },
  {
    "kanji": "婦",
    "meaning": "lady"
  },
  {
    "kanji": "掃",
    "meaning": "sweep"
  },
  {
    "kanji": "当",
    "meaning": "hit"
  },
  {
    "kanji": "争",
    "meaning": "contend"
  },
  {
    "kanji": "浄",
    "meaning": "clean"
  },
  {
    "kanji": "事",
    "meaning": "matter"
  },
  {
    "kanji": "唐",
    "meaning": "T'ang"
  },
  {
    "kanji": "糖",
    "meaning": "sugar"
  },
  {
    "kanji": "康",
    "meaning": "ease/sane"
  },
  {
    "kanji": "逮",
    "meaning": "apprehend"
  },
  {
    "kanji": "伊",
    "meaning": "Italy"
  },
  {
    "kanji": "君",
    "meaning": "old boy"
  },
  {
    "kanji": "群",
    "meaning": "flock"
  },
  {
    "kanji": "耐",
    "meaning": "#NAME?"
  },
  {
    "kanji": "需",
    "meaning": "demand"
  },
  {
    "kanji": "儒",
    "meaning": "Confucian"
  },
  {
    "kanji": "端",
    "meaning": "edge"
  },
  {
    "kanji": "両",
    "meaning": "both"
  },
  {
    "kanji": "満",
    "meaning": "full"
  },
  {
    "kanji": "画",
    "meaning": "brush stroke"
  },
  {
    "kanji": "歯",
    "meaning": "tooth"
  },
  {
    "kanji": "曲",
    "meaning": "bend"
  },
  {
    "kanji": "曹",
    "meaning": "cadet"
  },
  {
    "kanji": "遭",
    "meaning": "encounter"
  },
  {
    "kanji": "漕",
    "meaning": "rowing"
  },
  {
    "kanji": "槽",
    "meaning": "vat"
  },
  {
    "kanji": "斗",
    "meaning": "Big Dipper"
  },
  {
    "kanji": "料",
    "meaning": "fee"
  },
  {
    "kanji": "科",
    "meaning": "department"
  },
  {
    "kanji": "図",
    "meaning": "map"
  },
  {
    "kanji": "用",
    "meaning": "utilize"
  },
  {
    "kanji": "庸",
    "meaning": "commonplace/comfortable"
  },
  {
    "kanji": "備",
    "meaning": "equip"
  },
  {
    "kanji": "昔",
    "meaning": "once upon a time"
  },
  {
    "kanji": "錯",
    "meaning": "confused"
  },
  {
    "kanji": "借",
    "meaning": "borrow"
  },
  {
    "kanji": "惜",
    "meaning": "pity"
  },
  {
    "kanji": "措",
    "meaning": "set aside"
  },
  {
    "kanji": "散",
    "meaning": "scatter"
  },
  {
    "kanji": "廿",
    "meaning": "twenty"
  },
  {
    "kanji": "庶",
    "meaning": "commoner"
  },
  {
    "kanji": "遮",
    "meaning": "intercept"
  },
  {
    "kanji": "席",
    "meaning": "seat"
  },
  {
    "kanji": "度",
    "meaning": "degrees"
  },
  {
    "kanji": "渡",
    "meaning": "transit"
  },
  {
    "kanji": "奔",
    "meaning": "bustle"
  },
  {
    "kanji": "噴",
    "meaning": "erupt"
  },
  {
    "kanji": "墳",
    "meaning": "tomb"
  },
  {
    "kanji": "憤",
    "meaning": "aroused"
  },
  {
    "kanji": "焼",
    "meaning": "bake"
  },
  {
    "kanji": "暁",
    "meaning": "daybreak"
  },
  {
    "kanji": "半",
    "meaning": "half"
  },
  {
    "kanji": "伴",
    "meaning": "consort"
  },
  {
    "kanji": "畔",
    "meaning": "paddy-ridge"
  },
  {
    "kanji": "判",
    "meaning": "judgment"
  },
  {
    "kanji": "券",
    "meaning": "ticket"
  },
  {
    "kanji": "巻",
    "meaning": "scroll"
  },
  {
    "kanji": "圏",
    "meaning": "sphere"
  },
  {
    "kanji": "勝",
    "meaning": "victory"
  },
  {
    "kanji": "藤",
    "meaning": "wisteria"
  },
  {
    "kanji": "謄",
    "meaning": "mimeograph/facsimile"
  },
  {
    "kanji": "片",
    "meaning": "one-sided"
  },
  {
    "kanji": "版",
    "meaning": "printing block"
  },
  {
    "kanji": "之",
    "meaning": "of"
  },
  {
    "kanji": "乏",
    "meaning": "destitution"
  },
  {
    "kanji": "芝",
    "meaning": "turf"
  },
  {
    "kanji": "不",
    "meaning": "negative"
  },
  {
    "kanji": "否",
    "meaning": "negate"
  },
  {
    "kanji": "杯",
    "meaning": "cupfuls"
  },
  {
    "kanji": "矢",
    "meaning": "dart"
  },
  {
    "kanji": "矯",
    "meaning": "rectify"
  },
  {
    "kanji": "族",
    "meaning": "tribe"
  },
  {
    "kanji": "知",
    "meaning": "know"
  },
  {
    "kanji": "智",
    "meaning": "wisdom"
  },
  {
    "kanji": "矛",
    "meaning": "halberd"
  },
  {
    "kanji": "柔",
    "meaning": "tender"
  },
  {
    "kanji": "務",
    "meaning": "task"
  },
  {
    "kanji": "霧",
    "meaning": "fog"
  },
  {
    "kanji": "班",
    "meaning": "squad"
  },
  {
    "kanji": "帰",
    "meaning": "homecoming"
  },
  {
    "kanji": "弓",
    "meaning": "bow"
  },
  {
    "kanji": "引",
    "meaning": "pull"
  },
  {
    "kanji": "弔",
    "meaning": "condolences"
  },
  {
    "kanji": "弘",
    "meaning": "vast"
  },
  {
    "kanji": "強",
    "meaning": "strong"
  },
  {
    "kanji": "弱",
    "meaning": "weak"
  },
  {
    "kanji": "沸",
    "meaning": "seethe"
  },
  {
    "kanji": "費",
    "meaning": "expense"
  },
  {
    "kanji": "第",
    "meaning": "No."
  },
  {
    "kanji": "弟",
    "meaning": "younger brother"
  },
  {
    "kanji": "巧",
    "meaning": "adroit"
  },
  {
    "kanji": "号",
    "meaning": "nickname"
  },
  {
    "kanji": "朽",
    "meaning": "decay"
  },
  {
    "kanji": "誇",
    "meaning": "boast"
  },
  {
    "kanji": "汚",
    "meaning": "dirty"
  },
  {
    "kanji": "与",
    "meaning": "bestow"
  },
  {
    "kanji": "写",
    "meaning": "copy"
  },
  {
    "kanji": "身",
    "meaning": "somebody"
  },
  {
    "kanji": "射",
    "meaning": "shoot"
  },
  {
    "kanji": "謝",
    "meaning": "apologize"
  },
  {
    "kanji": "老",
    "meaning": "old man"
  },
  {
    "kanji": "考",
    "meaning": "consider"
  },
  {
    "kanji": "孝",
    "meaning": "filial piety"
  },
  {
    "kanji": "教",
    "meaning": "teach"
  },
  {
    "kanji": "拷",
    "meaning": "torture"
  },
  {
    "kanji": "者",
    "meaning": "someone"
  },
  {
    "kanji": "煮",
    "meaning": "boil"
  },
  {
    "kanji": "著",
    "meaning": "renowned"
  },
  {
    "kanji": "署",
    "meaning": "signature"
  },
  {
    "kanji": "暑",
    "meaning": "sultry"
  },
  {
    "kanji": "諸",
    "meaning": "various"
  },
  {
    "kanji": "猪",
    "meaning": "boar"
  },
  {
    "kanji": "渚",
    "meaning": "strand"
  },
  {
    "kanji": "賭",
    "meaning": "gamble"
  },
  {
    "kanji": "峡",
    "meaning": "gorge"
  },
  {
    "kanji": "狭",
    "meaning": "cramped"
  },
  {
    "kanji": "挟",
    "meaning": "sandwiched"
  },
  {
    "kanji": "追",
    "meaning": "chase"
  },
  {
    "kanji": "師",
    "meaning": "expert"
  },
  {
    "kanji": "帥",
    "meaning": "commander"
  },
  {
    "kanji": "官",
    "meaning": "bureaucrat"
  },
  {
    "kanji": "棺",
    "meaning": "coffin"
  },
  {
    "kanji": "管",
    "meaning": "pipe"
  },
  {
    "kanji": "父",
    "meaning": "father"
  },
  {
    "kanji": "交",
    "meaning": "mingle"
  },
  {
    "kanji": "効",
    "meaning": "merit"
  },
  {
    "kanji": "較",
    "meaning": "contrast"
  },
  {
    "kanji": "校",
    "meaning": "exam"
  },
  {
    "kanji": "足",
    "meaning": "leg"
  },
  {
    "kanji": "促",
    "meaning": "stimulate"
  },
  {
    "kanji": "距",
    "meaning": "long-distance"
  },
  {
    "kanji": "路",
    "meaning": "path"
  },
  {
    "kanji": "露",
    "meaning": "dew"
  },
  {
    "kanji": "跳",
    "meaning": "hop"
  },
  {
    "kanji": "躍",
    "meaning": "leap"
  },
  {
    "kanji": "践",
    "meaning": "tread"
  },
  {
    "kanji": "踏",
    "meaning": "step"
  },
  {
    "kanji": "骨",
    "meaning": "skeleton"
  },
  {
    "kanji": "滑",
    "meaning": "slippery"
  },
  {
    "kanji": "髄",
    "meaning": "marrow"
  },
  {
    "kanji": "禍",
    "meaning": "calamity"
  },
  {
    "kanji": "渦",
    "meaning": "whirlpool"
  },
  {
    "kanji": "過",
    "meaning": "overdo"
  },
  {
    "kanji": "阪",
    "meaning": "Heights"
  },
  {
    "kanji": "阿",
    "meaning": "Africa"
  },
  {
    "kanji": "際",
    "meaning": "occasion"
  },
  {
    "kanji": "障",
    "meaning": "hinder"
  },
  {
    "kanji": "随",
    "meaning": "follow"
  },
  {
    "kanji": "陪",
    "meaning": "obeisance/auxiliary"
  },
  {
    "kanji": "陽",
    "meaning": "sunshine"
  },
  {
    "kanji": "陳",
    "meaning": "exhibit/line up"
  },
  {
    "kanji": "防",
    "meaning": "ward off"
  },
  {
    "kanji": "附",
    "meaning": "affixed"
  },
  {
    "kanji": "院",
    "meaning": "Inst."
  },
  {
    "kanji": "陣",
    "meaning": "camp"
  },
  {
    "kanji": "隊",
    "meaning": "regiment"
  },
  {
    "kanji": "墜",
    "meaning": "crash"
  },
  {
    "kanji": "降",
    "meaning": "descend"
  },
  {
    "kanji": "階",
    "meaning": "storey"
  },
  {
    "kanji": "陛",
    "meaning": "highness"
  },
  {
    "kanji": "隣",
    "meaning": "neighboring"
  },
  {
    "kanji": "隔",
    "meaning": "isolate"
  },
  {
    "kanji": "隠",
    "meaning": "conceal"
  },
  {
    "kanji": "堕",
    "meaning": "degenerate"
  },
  {
    "kanji": "陥",
    "meaning": "collapse"
  },
  {
    "kanji": "穴",
    "meaning": "hole"
  },
  {
    "kanji": "空",
    "meaning": "empty"
  },
  {
    "kanji": "控",
    "meaning": "withdraw"
  },
  {
    "kanji": "突",
    "meaning": "stab"
  },
  {
    "kanji": "究",
    "meaning": "research"
  },
  {
    "kanji": "窒",
    "meaning": "plug up"
  },
  {
    "kanji": "窃",
    "meaning": "stealth"
  },
  {
    "kanji": "窪",
    "meaning": "depression"
  },
  {
    "kanji": "搾",
    "meaning": "squeeze"
  },
  {
    "kanji": "窯",
    "meaning": "kiln"
  },
  {
    "kanji": "窮",
    "meaning": "hard up"
  },
  {
    "kanji": "探",
    "meaning": "grope"
  },
  {
    "kanji": "深",
    "meaning": "deep"
  },
  {
    "kanji": "丘",
    "meaning": "hill"
  },
  {
    "kanji": "岳",
    "meaning": "Point"
  },
  {
    "kanji": "兵",
    "meaning": "soldier"
  },
  {
    "kanji": "浜",
    "meaning": "seacoast"
  },
  {
    "kanji": "糸",
    "meaning": "thread"
  },
  {
    "kanji": "織",
    "meaning": "weave"
  },
  {
    "kanji": "繕",
    "meaning": "darning"
  },
  {
    "kanji": "縮",
    "meaning": "shrink"
  },
  {
    "kanji": "繁",
    "meaning": "luxuriant"
  },
  {
    "kanji": "縦",
    "meaning": "vertical"
  },
  {
    "kanji": "線",
    "meaning": "line"
  },
  {
    "kanji": "締",
    "meaning": "tighten"
  },
  {
    "kanji": "維",
    "meaning": "fiber"
  },
  {
    "kanji": "羅",
    "meaning": "gauze"
  },
  {
    "kanji": "練",
    "meaning": "practice"
  },
  {
    "kanji": "緒",
    "meaning": "thong"
  },
  {
    "kanji": "続",
    "meaning": "continue"
  },
  {
    "kanji": "絵",
    "meaning": "picture"
  },
  {
    "kanji": "統",
    "meaning": "overall"
  },
  {
    "kanji": "絞",
    "meaning": "strangle"
  },
  {
    "kanji": "給",
    "meaning": "salary"
  },
  {
    "kanji": "絡",
    "meaning": "entwine"
  },
  {
    "kanji": "結",
    "meaning": "tie"
  },
  {
    "kanji": "終",
    "meaning": "end"
  },
  {
    "kanji": "級",
    "meaning": "class"
  },
  {
    "kanji": "紀",
    "meaning": "chronicle"
  },
  {
    "kanji": "紅",
    "meaning": "crimson"
  },
  {
    "kanji": "納",
    "meaning": "settlement"
  },
  {
    "kanji": "紡",
    "meaning": "spinning"
  },
  {
    "kanji": "紛",
    "meaning": "distract"
  },
  {
    "kanji": "紹",
    "meaning": "introduce"
  },
  {
    "kanji": "経",
    "meaning": "sutra"
  },
  {
    "kanji": "紳",
    "meaning": "sire"
  },
  {
    "kanji": "約",
    "meaning": "promise"
  },
  {
    "kanji": "細",
    "meaning": "dainty"
  },
  {
    "kanji": "累",
    "meaning": "accumulate"
  },
  {
    "kanji": "索",
    "meaning": "cord"
  },
  {
    "kanji": "総",
    "meaning": "general"
  },
  {
    "kanji": "綿",
    "meaning": "cotton"
  },
  {
    "kanji": "絹",
    "meaning": "silk"
  },
  {
    "kanji": "繰",
    "meaning": "winding"
  },
  {
    "kanji": "継",
    "meaning": "inherit"
  },
  {
    "kanji": "緑",
    "meaning": "green"
  },
  {
    "kanji": "縁",
    "meaning": "affinity"
  },
  {
    "kanji": "網",
    "meaning": "netting"
  },
  {
    "kanji": "緊",
    "meaning": "tense"
  },
  {
    "kanji": "紫",
    "meaning": "purple"
  },
  {
    "kanji": "縛",
    "meaning": "truss"
  },
  {
    "kanji": "縄",
    "meaning": "straw rope"
  },
  {
    "kanji": "幼",
    "meaning": "infancy"
  },
  {
    "kanji": "後",
    "meaning": "behind"
  },
  {
    "kanji": "幽",
    "meaning": "seclude/faint"
  },
  {
    "kanji": "幾",
    "meaning": "how many"
  },
  {
    "kanji": "機",
    "meaning": "mechanism"
  },
  {
    "kanji": "玄",
    "meaning": "mysterious"
  },
  {
    "kanji": "畜",
    "meaning": "livestock"
  },
  {
    "kanji": "蓄",
    "meaning": "amass"
  },
  {
    "kanji": "弦",
    "meaning": "bowstring"
  },
  {
    "kanji": "擁",
    "meaning": "hug"
  },
  {
    "kanji": "滋",
    "meaning": "nourishing"
  },
  {
    "kanji": "慈",
    "meaning": "mercy"
  },
  {
    "kanji": "磁",
    "meaning": "magnet"
  },
  {
    "kanji": "系",
    "meaning": "lineage"
  },
  {
    "kanji": "係",
    "meaning": "person in charge"
  },
  {
    "kanji": "孫",
    "meaning": "grandchild"
  },
  {
    "kanji": "懸",
    "meaning": "suspend"
  },
  {
    "kanji": "却",
    "meaning": "instead"
  },
  {
    "kanji": "脚",
    "meaning": "skids/shins"
  },
  {
    "kanji": "卸",
    "meaning": "wholesale"
  },
  {
    "kanji": "御",
    "meaning": "honorable"
  },
  {
    "kanji": "服",
    "meaning": "clothing"
  },
  {
    "kanji": "命",
    "meaning": "fate"
  },
  {
    "kanji": "令",
    "meaning": "orders"
  },
  {
    "kanji": "零",
    "meaning": "zero"
  },
  {
    "kanji": "齢",
    "meaning": "age"
  },
  {
    "kanji": "冷",
    "meaning": "cool"
  },
  {
    "kanji": "領",
    "meaning": "jurisdiction"
  },
  {
    "kanji": "鈴",
    "meaning": "small bell"
  },
  {
    "kanji": "勇",
    "meaning": "courage"
  },
  {
    "kanji": "通",
    "meaning": "traffic"
  },
  {
    "kanji": "踊",
    "meaning": "jump"
  },
  {
    "kanji": "疑",
    "meaning": "doubt"
  },
  {
    "kanji": "擬",
    "meaning": "mimic"
  },
  {
    "kanji": "凝",
    "meaning": "congeal"
  },
  {
    "kanji": "範",
    "meaning": "pattern"
  },
  {
    "kanji": "犯",
    "meaning": "crime"
  },
  {
    "kanji": "厄",
    "meaning": "unlucky"
  },
  {
    "kanji": "危",
    "meaning": "dangerous"
  },
  {
    "kanji": "宛",
    "meaning": "address"
  },
  {
    "kanji": "腕",
    "meaning": "arm"
  },
  {
    "kanji": "苑",
    "meaning": "garden"
  },
  {
    "kanji": "怨",
    "meaning": "grudge"
  },
  {
    "kanji": "柳",
    "meaning": "willow"
  },
  {
    "kanji": "卵",
    "meaning": "egg"
  },
  {
    "kanji": "留",
    "meaning": "detain"
  },
  {
    "kanji": "貿",
    "meaning": "trade"
  },
  {
    "kanji": "印",
    "meaning": "stamp"
  },
  {
    "kanji": "興",
    "meaning": "entertain"
  },
  {
    "kanji": "酉",
    "meaning": "sign of the bird"
  },
  {
    "kanji": "酒",
    "meaning": "sake"
  },
  {
    "kanji": "酌",
    "meaning": "bartending"
  },
  {
    "kanji": "酵",
    "meaning": "fermentation"
  },
  {
    "kanji": "酷",
    "meaning": "cruel"
  },
  {
    "kanji": "酬",
    "meaning": "repay"
  },
  {
    "kanji": "酪",
    "meaning": "dairy products"
  },
  {
    "kanji": "酢",
    "meaning": "vinegar"
  },
  {
    "kanji": "酔",
    "meaning": "drunk"
  },
  {
    "kanji": "配",
    "meaning": "distribute"
  },
  {
    "kanji": "酸",
    "meaning": "acid"
  },
  {
    "kanji": "猶",
    "meaning": "furthermore/waver"
  },
  {
    "kanji": "尊",
    "meaning": "revered"
  },
  {
    "kanji": "豆",
    "meaning": "beans"
  },
  {
    "kanji": "頭",
    "meaning": "head"
  },
  {
    "kanji": "短",
    "meaning": "short"
  },
  {
    "kanji": "豊",
    "meaning": "bountiful"
  },
  {
    "kanji": "鼓",
    "meaning": "drum"
  },
  {
    "kanji": "喜",
    "meaning": "rejoice"
  },
  {
    "kanji": "樹",
    "meaning": "timber-trees"
  },
  {
    "kanji": "皿",
    "meaning": "dish"
  },
  {
    "kanji": "血",
    "meaning": "blood"
  },
  {
    "kanji": "盆",
    "meaning": "basin"
  },
  {
    "kanji": "盟",
    "meaning": "alliance"
  },
  {
    "kanji": "盗",
    "meaning": "steal"
  },
  {
    "kanji": "温",
    "meaning": "warm"
  },
  {
    "kanji": "監",
    "meaning": "oversee"
  },
  {
    "kanji": "濫",
    "meaning": "overflow"
  },
  {
    "kanji": "鑑",
    "meaning": "specimen"
  },
  {
    "kanji": "猛",
    "meaning": "fierce"
  },
  {
    "kanji": "盛",
    "meaning": "boom"
  },
  {
    "kanji": "塩",
    "meaning": "salt"
  },
  {
    "kanji": "銀",
    "meaning": "silver"
  },
  {
    "kanji": "恨",
    "meaning": "regret/resentment"
  },
  {
    "kanji": "根",
    "meaning": "root"
  },
  {
    "kanji": "即",
    "meaning": "instant"
  },
  {
    "kanji": "爵",
    "meaning": "baron"
  },
  {
    "kanji": "節",
    "meaning": "node"
  },
  {
    "kanji": "退",
    "meaning": "retreat"
  },
  {
    "kanji": "限",
    "meaning": "limit"
  },
  {
    "kanji": "眼",
    "meaning": "eyeball"
  },
  {
    "kanji": "良",
    "meaning": "good"
  },
  {
    "kanji": "朗",
    "meaning": "melodious"
  },
  {
    "kanji": "浪",
    "meaning": "wandering"
  },
  {
    "kanji": "娘",
    "meaning": "daughter"
  },
  {
    "kanji": "食",
    "meaning": "eat"
  },
  {
    "kanji": "飯",
    "meaning": "meal"
  },
  {
    "kanji": "飲",
    "meaning": "drink"
  },
  {
    "kanji": "飢",
    "meaning": "hungry"
  },
  {
    "kanji": "餓",
    "meaning": "starve"
  },
  {
    "kanji": "飾",
    "meaning": "decorate"
  },
  {
    "kanji": "館",
    "meaning": "Bldg."
  },
  {
    "kanji": "養",
    "meaning": "foster"
  },
  {
    "kanji": "飽",
    "meaning": "sated"
  },
  {
    "kanji": "既",
    "meaning": "previously"
  },
  {
    "kanji": "概",
    "meaning": "outline"
  },
  {
    "kanji": "慨",
    "meaning": "rue"
  },
  {
    "kanji": "平",
    "meaning": "even"
  },
  {
    "kanji": "呼",
    "meaning": "call"
  },
  {
    "kanji": "坪",
    "meaning": "two-mat area"
  },
  {
    "kanji": "評",
    "meaning": "evaluate"
  },
  {
    "kanji": "刈",
    "meaning": "reap"
  },
  {
    "kanji": "希",
    "meaning": "hope"
  },
  {
    "kanji": "凶",
    "meaning": "villain"
  },
  {
    "kanji": "胸",
    "meaning": "bosom"
  },
  {
    "kanji": "離",
    "meaning": "detach"
  },
  {
    "kanji": "殺",
    "meaning": "kill"
  },
  {
    "kanji": "純",
    "meaning": "genuine"
  },
  {
    "kanji": "鈍",
    "meaning": "dull"
  },
  {
    "kanji": "辛",
    "meaning": "spicy"
  },
  {
    "kanji": "辞",
    "meaning": "resign"
  },
  {
    "kanji": "梓",
    "meaning": "catalpa"
  },
  {
    "kanji": "宰",
    "meaning": "superintend"
  },
  {
    "kanji": "壁",
    "meaning": "wall"
  },
  {
    "kanji": "避",
    "meaning": "evade"
  },
  {
    "kanji": "新",
    "meaning": "new"
  },
  {
    "kanji": "薪",
    "meaning": "fuel/firewood"
  },
  {
    "kanji": "親",
    "meaning": "parent"
  },
  {
    "kanji": "幸",
    "meaning": "happiness"
  },
  {
    "kanji": "執",
    "meaning": "tenacious"
  },
  {
    "kanji": "報",
    "meaning": "report"
  },
  {
    "kanji": "叫",
    "meaning": "shout"
  },
  {
    "kanji": "糾",
    "meaning": "twist"
  },
  {
    "kanji": "収",
    "meaning": "income"
  },
  {
    "kanji": "卑",
    "meaning": "lowly"
  },
  {
    "kanji": "碑",
    "meaning": "tombstone"
  },
  {
    "kanji": "陸",
    "meaning": "land"
  },
  {
    "kanji": "睦",
    "meaning": "intimate"
  },
  {
    "kanji": "勢",
    "meaning": "forces"
  },
  {
    "kanji": "熱",
    "meaning": "heat"
  },
  {
    "kanji": "菱",
    "meaning": "diamond"
  },
  {
    "kanji": "陵",
    "meaning": "mausoleum"
  },
  {
    "kanji": "亥",
    "meaning": "sign of the hog"
  },
  {
    "kanji": "核",
    "meaning": "nucleus"
  },
  {
    "kanji": "刻",
    "meaning": "engrave"
  },
  {
    "kanji": "該",
    "meaning": "above-stated"
  },
  {
    "kanji": "劾",
    "meaning": "censure"
  },
  {
    "kanji": "述",
    "meaning": "mention"
  },
  {
    "kanji": "術",
    "meaning": "art"
  },
  {
    "kanji": "寒",
    "meaning": "cold"
  },
  {
    "kanji": "醸",
    "meaning": "brew"
  },
  {
    "kanji": "譲",
    "meaning": "defer"
  },
  {
    "kanji": "壌",
    "meaning": "lot"
  },
  {
    "kanji": "嬢",
    "meaning": "lass"
  },
  {
    "kanji": "毒",
    "meaning": "poison"
  },
  {
    "kanji": "素",
    "meaning": "elementary"
  },
  {
    "kanji": "麦",
    "meaning": "barley"
  },
  {
    "kanji": "青",
    "meaning": "blue"
  },
  {
    "kanji": "精",
    "meaning": "refined"
  },
  {
    "kanji": "請",
    "meaning": "solicit"
  },
  {
    "kanji": "情",
    "meaning": "feelings"
  },
  {
    "kanji": "晴",
    "meaning": "clear up"
  },
  {
    "kanji": "清",
    "meaning": "pure"
  },
  {
    "kanji": "静",
    "meaning": "quiet"
  },
  {
    "kanji": "責",
    "meaning": "blame"
  },
  {
    "kanji": "績",
    "meaning": "exploits"
  },
  {
    "kanji": "積",
    "meaning": "volume"
  },
  {
    "kanji": "債",
    "meaning": "bond"
  },
  {
    "kanji": "漬",
    "meaning": "pickling"
  },
  {
    "kanji": "表",
    "meaning": "surface"
  },
  {
    "kanji": "俵",
    "meaning": "bag"
  },
  {
    "kanji": "潔",
    "meaning": "undefiled"
  },
  {
    "kanji": "契",
    "meaning": "pledge"
  },
  {
    "kanji": "喫",
    "meaning": "consume"
  },
  {
    "kanji": "害",
    "meaning": "harm"
  },
  {
    "kanji": "轄",
    "meaning": "control"
  },
  {
    "kanji": "割",
    "meaning": "proportion"
  },
  {
    "kanji": "憲",
    "meaning": "constitution"
  },
  {
    "kanji": "生",
    "meaning": "life"
  },
  {
    "kanji": "星",
    "meaning": "star"
  },
  {
    "kanji": "姓",
    "meaning": "surname"
  },
  {
    "kanji": "性",
    "meaning": "sex"
  },
  {
    "kanji": "牲",
    "meaning": "animal sacrifice"
  },
  {
    "kanji": "産",
    "meaning": "products"
  },
  {
    "kanji": "隆",
    "meaning": "hump"
  },
  {
    "kanji": "峰",
    "meaning": "summit"
  },
  {
    "kanji": "縫",
    "meaning": "sew"
  },
  {
    "kanji": "拝",
    "meaning": "worship"
  },
  {
    "kanji": "寿",
    "meaning": "longevity"
  },
  {
    "kanji": "鋳",
    "meaning": "casting"
  },
  {
    "kanji": "籍",
    "meaning": "enroll"
  },
  {
    "kanji": "春",
    "meaning": "springtime"
  },
  {
    "kanji": "椿",
    "meaning": "camellia"
  },
  {
    "kanji": "泰",
    "meaning": "peaceful"
  },
  {
    "kanji": "奏",
    "meaning": "play music"
  },
  {
    "kanji": "実",
    "meaning": "reality"
  },
  {
    "kanji": "奉",
    "meaning": "observance/dedicate"
  },
  {
    "kanji": "俸",
    "meaning": "stipend"
  },
  {
    "kanji": "棒",
    "meaning": "rod"
  },
  {
    "kanji": "謹",
    "meaning": "discreet"
  },
  {
    "kanji": "勤",
    "meaning": "diligence"
  },
  {
    "kanji": "漢",
    "meaning": "Sino-"
  },
  {
    "kanji": "嘆",
    "meaning": "sigh"
  },
  {
    "kanji": "難",
    "meaning": "difficult"
  },
  {
    "kanji": "華",
    "meaning": "splendor"
  },
  {
    "kanji": "垂",
    "meaning": "droop"
  },
  {
    "kanji": "睡",
    "meaning": "drowsy"
  },
  {
    "kanji": "錘",
    "meaning": "spindle"
  },
  {
    "kanji": "乗",
    "meaning": "ride"
  },
  {
    "kanji": "剰",
    "meaning": "surplus"
  },
  {
    "kanji": "今",
    "meaning": "now"
  },
  {
    "kanji": "含",
    "meaning": "include"
  },
  {
    "kanji": "吟",
    "meaning": "versify"
  },
  {
    "kanji": "念",
    "meaning": "wish"
  },
  {
    "kanji": "琴",
    "meaning": "harp"
  },
  {
    "kanji": "陰",
    "meaning": "shade"
  },
  {
    "kanji": "予",
    "meaning": "beforehand"
  },
  {
    "kanji": "序",
    "meaning": "preface"
  },
  {
    "kanji": "預",
    "meaning": "deposit"
  },
  {
    "kanji": "野",
    "meaning": "plains"
  },
  {
    "kanji": "兼",
    "meaning": "concurrently"
  },
  {
    "kanji": "嫌",
    "meaning": "dislike"
  },
  {
    "kanji": "鎌",
    "meaning": "sickle"
  },
  {
    "kanji": "謙",
    "meaning": "self-effacing"
  },
  {
    "kanji": "廉",
    "meaning": "bargain"
  },
  {
    "kanji": "西",
    "meaning": "west"
  },
  {
    "kanji": "価",
    "meaning": "value"
  },
  {
    "kanji": "要",
    "meaning": "need"
  },
  {
    "kanji": "腰",
    "meaning": "loins"
  },
  {
    "kanji": "票",
    "meaning": "ballot"
  },
  {
    "kanji": "漂",
    "meaning": "drift"
  },
  {
    "kanji": "標",
    "meaning": "signpost"
  },
  {
    "kanji": "栗",
    "meaning": "chestnut"
  },
  {
    "kanji": "遷",
    "meaning": "transition"
  },
  {
    "kanji": "覆",
    "meaning": "capsize"
  },
  {
    "kanji": "煙",
    "meaning": "smoke"
  },
  {
    "kanji": "南",
    "meaning": "south"
  },
  {
    "kanji": "楠",
    "meaning": "camphor tree"
  },
  {
    "kanji": "献",
    "meaning": "offering"
  },
  {
    "kanji": "門",
    "meaning": "gates"
  },
  {
    "kanji": "問",
    "meaning": "question"
  },
  {
    "kanji": "閲",
    "meaning": "review"
  },
  {
    "kanji": "閥",
    "meaning": "clique"
  },
  {
    "kanji": "間",
    "meaning": "interval"
  },
  {
    "kanji": "簡",
    "meaning": "simplicity"
  },
  {
    "kanji": "開",
    "meaning": "open"
  },
  {
    "kanji": "閉",
    "meaning": "closed"
  },
  {
    "kanji": "閣",
    "meaning": "tower"
  },
  {
    "kanji": "閑",
    "meaning": "leisure"
  },
  {
    "kanji": "聞",
    "meaning": "hear"
  },
  {
    "kanji": "潤",
    "meaning": "wet"
  },
  {
    "kanji": "欄",
    "meaning": "column"
  },
  {
    "kanji": "闘",
    "meaning": "fight"
  },
  {
    "kanji": "倉",
    "meaning": "godown"
  },
  {
    "kanji": "創",
    "meaning": "genesis"
  },
  {
    "kanji": "非",
    "meaning": "un-"
  },
  {
    "kanji": "俳",
    "meaning": "haiku"
  },
  {
    "kanji": "排",
    "meaning": "repudiate"
  },
  {
    "kanji": "悲",
    "meaning": "sad"
  },
  {
    "kanji": "罪",
    "meaning": "guilt"
  },
  {
    "kanji": "輩",
    "meaning": "comrade"
  },
  {
    "kanji": "扉",
    "meaning": "front door"
  },
  {
    "kanji": "侯",
    "meaning": "marquis"
  },
  {
    "kanji": "候",
    "meaning": "climate"
  },
  {
    "kanji": "決",
    "meaning": "decide"
  },
  {
    "kanji": "快",
    "meaning": "cheerful"
  },
  {
    "kanji": "偉",
    "meaning": "admirable"
  },
  {
    "kanji": "違",
    "meaning": "difference"
  },
  {
    "kanji": "緯",
    "meaning": "horizontal"
  },
  {
    "kanji": "衛",
    "meaning": "defense"
  },
  {
    "kanji": "韓",
    "meaning": "Korea"
  },
  {
    "kanji": "干",
    "meaning": "dry"
  },
  {
    "kanji": "肝",
    "meaning": "liver"
  },
  {
    "kanji": "刊",
    "meaning": "publish"
  },
  {
    "kanji": "汗",
    "meaning": "sweat"
  },
  {
    "kanji": "軒",
    "meaning": "flats"
  },
  {
    "kanji": "岸",
    "meaning": "beach"
  },
  {
    "kanji": "幹",
    "meaning": "tree-trunk"
  },
  {
    "kanji": "芋",
    "meaning": "potato"
  },
  {
    "kanji": "宇",
    "meaning": "eaves"
  },
  {
    "kanji": "余",
    "meaning": "too much"
  },
  {
    "kanji": "除",
    "meaning": "exclude"
  },
  {
    "kanji": "徐",
    "meaning": "gradually"
  },
  {
    "kanji": "叙",
    "meaning": "confer"
  },
  {
    "kanji": "途",
    "meaning": "route"
  },
  {
    "kanji": "斜",
    "meaning": "diagonal"
  },
  {
    "kanji": "塗",
    "meaning": "paint"
  },
  {
    "kanji": "束",
    "meaning": "bundle"
  },
  {
    "kanji": "頼",
    "meaning": "trust"
  },
  {
    "kanji": "瀬",
    "meaning": "rapids"
  },
  {
    "kanji": "勅",
    "meaning": "imperial order"
  },
  {
    "kanji": "疎",
    "meaning": "alienate"
  },
  {
    "kanji": "速",
    "meaning": "quick"
  },
  {
    "kanji": "整",
    "meaning": "organize"
  },
  {
    "kanji": "剣",
    "meaning": "sabre/saber"
  },
  {
    "kanji": "険",
    "meaning": "precipitous"
  },
  {
    "kanji": "検",
    "meaning": "examination"
  },
  {
    "kanji": "倹",
    "meaning": "frugal"
  },
  {
    "kanji": "重",
    "meaning": "heavy"
  },
  {
    "kanji": "動",
    "meaning": "move"
  },
  {
    "kanji": "勲",
    "meaning": "meritorious deed"
  },
  {
    "kanji": "働",
    "meaning": "work"
  },
  {
    "kanji": "種",
    "meaning": "species"
  },
  {
    "kanji": "衝",
    "meaning": "collide"
  },
  {
    "kanji": "薫",
    "meaning": "fragrant"
  },
  {
    "kanji": "病",
    "meaning": "ill"
  },
  {
    "kanji": "痴",
    "meaning": "stupid"
  },
  {
    "kanji": "痘",
    "meaning": "pox"
  },
  {
    "kanji": "症",
    "meaning": "symptoms"
  },
  {
    "kanji": "疾",
    "meaning": "rapidly"
  },
  {
    "kanji": "痢",
    "meaning": "diarrhea"
  },
  {
    "kanji": "疲",
    "meaning": "exhausted/tired"
  },
  {
    "kanji": "疫",
    "meaning": "epidemic"
  },
  {
    "kanji": "痛",
    "meaning": "pain"
  },
  {
    "kanji": "癖",
    "meaning": "mannerism"
  },
  {
    "kanji": "匿",
    "meaning": "hide"
  },
  {
    "kanji": "匠",
    "meaning": "artisan"
  },
  {
    "kanji": "医",
    "meaning": "doctor"
  },
  {
    "kanji": "匹",
    "meaning": "equal"
  },
  {
    "kanji": "区",
    "meaning": "ward"
  },
  {
    "kanji": "枢",
    "meaning": "hinge"
  },
  {
    "kanji": "殴",
    "meaning": "assault"
  },
  {
    "kanji": "欧",
    "meaning": "Europe"
  },
  {
    "kanji": "抑",
    "meaning": "repress"
  },
  {
    "kanji": "仰",
    "meaning": "face-up"
  },
  {
    "kanji": "迎",
    "meaning": "welcome"
  },
  {
    "kanji": "登",
    "meaning": "ascend"
  },
  {
    "kanji": "澄",
    "meaning": "lucidity"
  },
  {
    "kanji": "発",
    "meaning": "discharge"
  },
  {
    "kanji": "廃",
    "meaning": "abolish"
  },
  {
    "kanji": "僚",
    "meaning": "colleague"
  },
  {
    "kanji": "寮",
    "meaning": "dormitory"
  },
  {
    "kanji": "療",
    "meaning": "heal"
  },
  {
    "kanji": "彫",
    "meaning": "carve"
  },
  {
    "kanji": "形",
    "meaning": "shape"
  },
  {
    "kanji": "影",
    "meaning": "shadow"
  },
  {
    "kanji": "杉",
    "meaning": "cedar"
  },
  {
    "kanji": "彩",
    "meaning": "coloring"
  },
  {
    "kanji": "彰",
    "meaning": "patent"
  },
  {
    "kanji": "彦",
    "meaning": "lad"
  },
  {
    "kanji": "顔",
    "meaning": "face"
  },
  {
    "kanji": "須",
    "meaning": "ought"
  },
  {
    "kanji": "膨",
    "meaning": "swell"
  },
  {
    "kanji": "参",
    "meaning": "nonplussed/visit"
  },
  {
    "kanji": "惨",
    "meaning": "wretched"
  },
  {
    "kanji": "修",
    "meaning": "discipline"
  },
  {
    "kanji": "珍",
    "meaning": "rare"
  },
  {
    "kanji": "診",
    "meaning": "check-up"
  },
  {
    "kanji": "文",
    "meaning": "sentence"
  },
  {
    "kanji": "対",
    "meaning": "vis-a-vis"
  },
  {
    "kanji": "紋",
    "meaning": "family crest"
  },
  {
    "kanji": "蚊",
    "meaning": "mosquito"
  },
  {
    "kanji": "斉",
    "meaning": "adjusted"
  },
  {
    "kanji": "剤",
    "meaning": "dose"
  },
  {
    "kanji": "済",
    "meaning": "finish"
  },
  {
    "kanji": "斎",
    "meaning": "purification"
  },
  {
    "kanji": "粛",
    "meaning": "solemn"
  },
  {
    "kanji": "塁",
    "meaning": "bases"
  },
  {
    "kanji": "楽",
    "meaning": "music"
  },
  {
    "kanji": "薬",
    "meaning": "medicine"
  },
  {
    "kanji": "率",
    "meaning": "ratio"
  },
  {
    "kanji": "渋",
    "meaning": "astringent"
  },
  {
    "kanji": "摂",
    "meaning": "vicarious"
  },
  {
    "kanji": "央",
    "meaning": "center"
  },
  {
    "kanji": "英",
    "meaning": "England"
  },
  {
    "kanji": "映",
    "meaning": "reflect"
  },
  {
    "kanji": "赤",
    "meaning": "red"
  },
  {
    "kanji": "赦",
    "meaning": "pardon"
  },
  {
    "kanji": "変",
    "meaning": "unusual"
  },
  {
    "kanji": "跡",
    "meaning": "tracks"
  },
  {
    "kanji": "蛮",
    "meaning": "barbarian"
  },
  {
    "kanji": "恋",
    "meaning": "romance"
  },
  {
    "kanji": "湾",
    "meaning": "gulf"
  },
  {
    "kanji": "黄",
    "meaning": "yellow"
  },
  {
    "kanji": "横",
    "meaning": "sideways"
  },
  {
    "kanji": "把",
    "meaning": "grasp"
  },
  {
    "kanji": "色",
    "meaning": "color"
  },
  {
    "kanji": "絶",
    "meaning": "discontinue"
  },
  {
    "kanji": "艶",
    "meaning": "glossy"
  },
  {
    "kanji": "肥",
    "meaning": "fertilizer"
  },
  {
    "kanji": "甘",
    "meaning": "sweet"
  },
  {
    "kanji": "紺",
    "meaning": "navy blue"
  },
  {
    "kanji": "某",
    "meaning": "so-and-so"
  },
  {
    "kanji": "謀",
    "meaning": "conspire"
  },
  {
    "kanji": "媒",
    "meaning": "mediator"
  },
  {
    "kanji": "欺",
    "meaning": "deceit"
  },
  {
    "kanji": "棋",
    "meaning": "chess piece"
  },
  {
    "kanji": "旗",
    "meaning": "national flag"
  },
  {
    "kanji": "期",
    "meaning": "period"
  },
  {
    "kanji": "碁",
    "meaning": "Go"
  },
  {
    "kanji": "基",
    "meaning": "fundamentals"
  },
  {
    "kanji": "甚",
    "meaning": "tremendously"
  },
  {
    "kanji": "勘",
    "meaning": "intuition"
  },
  {
    "kanji": "堪",
    "meaning": "withstand"
  },
  {
    "kanji": "貴",
    "meaning": "precious"
  },
  {
    "kanji": "遺",
    "meaning": "bequeath"
  },
  {
    "kanji": "遣",
    "meaning": "dispatch"
  },
  {
    "kanji": "舞",
    "meaning": "dance"
  },
  {
    "kanji": "無",
    "meaning": "nothingness"
  },
  {
    "kanji": "組",
    "meaning": "association"
  },
  {
    "kanji": "粗",
    "meaning": "coarse"
  },
  {
    "kanji": "租",
    "meaning": "tariff"
  },
  {
    "kanji": "祖",
    "meaning": "ancestor"
  },
  {
    "kanji": "阻",
    "meaning": "thwart"
  },
  {
    "kanji": "査",
    "meaning": "investigate"
  },
  {
    "kanji": "助",
    "meaning": "help"
  },
  {
    "kanji": "宜",
    "meaning": "best regards"
  },
  {
    "kanji": "畳",
    "meaning": "tatami mat"
  },
  {
    "kanji": "並",
    "meaning": "row"
  },
  {
    "kanji": "普",
    "meaning": "universal"
  },
  {
    "kanji": "譜",
    "meaning": "musical score"
  },
  {
    "kanji": "湿",
    "meaning": "damp"
  },
  {
    "kanji": "顕",
    "meaning": "appear"
  },
  {
    "kanji": "繊",
    "meaning": "slender"
  },
  {
    "kanji": "霊",
    "meaning": "spirits"
  },
  {
    "kanji": "業",
    "meaning": "business/profession"
  },
  {
    "kanji": "撲",
    "meaning": "slap"
  },
  {
    "kanji": "僕",
    "meaning": "me"
  },
  {
    "kanji": "共",
    "meaning": "together"
  },
  {
    "kanji": "供",
    "meaning": "submit"
  },
  {
    "kanji": "異",
    "meaning": "uncommon"
  },
  {
    "kanji": "翼",
    "meaning": "wing"
  },
  {
    "kanji": "洪",
    "meaning": "deluge"
  },
  {
    "kanji": "港",
    "meaning": "harbor"
  },
  {
    "kanji": "暴",
    "meaning": "outburst"
  },
  {
    "kanji": "爆",
    "meaning": "bomb"
  },
  {
    "kanji": "恭",
    "meaning": "respect"
  },
  {
    "kanji": "選",
    "meaning": "elect"
  },
  {
    "kanji": "殿",
    "meaning": "Mr."
  },
  {
    "kanji": "井",
    "meaning": "well"
  },
  {
    "kanji": "囲",
    "meaning": "surround"
  },
  {
    "kanji": "耕",
    "meaning": "till"
  },
  {
    "kanji": "亜",
    "meaning": "Asia"
  },
  {
    "kanji": "悪",
    "meaning": "bad"
  },
  {
    "kanji": "円",
    "meaning": "circle"
  },
  {
    "kanji": "角",
    "meaning": "angle"
  },
  {
    "kanji": "触",
    "meaning": "contact"
  },
  {
    "kanji": "解",
    "meaning": "unravel"
  },
  {
    "kanji": "再",
    "meaning": "again"
  },
  {
    "kanji": "講",
    "meaning": "lecture"
  },
  {
    "kanji": "購",
    "meaning": "subscription"
  },
  {
    "kanji": "構",
    "meaning": "posture"
  },
  {
    "kanji": "溝",
    "meaning": "gutter"
  },
  {
    "kanji": "論",
    "meaning": "argument"
  },
  {
    "kanji": "倫",
    "meaning": "ethics"
  },
  {
    "kanji": "輪",
    "meaning": "wheel"
  },
  {
    "kanji": "偏",
    "meaning": "partial"
  },
  {
    "kanji": "遍",
    "meaning": "everywhere"
  },
  {
    "kanji": "編",
    "meaning": "compilation"
  },
  {
    "kanji": "冊",
    "meaning": "tome"
  },
  {
    "kanji": "典",
    "meaning": "code"
  },
  {
    "kanji": "氏",
    "meaning": "family name"
  },
  {
    "kanji": "紙",
    "meaning": "paper"
  },
  {
    "kanji": "婚",
    "meaning": "marriage"
  },
  {
    "kanji": "低",
    "meaning": "lower"
  },
  {
    "kanji": "抵",
    "meaning": "resist"
  },
  {
    "kanji": "底",
    "meaning": "bottom"
  },
  {
    "kanji": "民",
    "meaning": "people"
  },
  {
    "kanji": "眠",
    "meaning": "sleep"
  },
  {
    "kanji": "捕",
    "meaning": "catch"
  },
  {
    "kanji": "浦",
    "meaning": "bay"
  },
  {
    "kanji": "蒲",
    "meaning": "bulrush"
  },
  {
    "kanji": "舗",
    "meaning": "shop"
  },
  {
    "kanji": "補",
    "meaning": "supplement"
  },
  {
    "kanji": "邸",
    "meaning": "residence"
  },
  {
    "kanji": "郭",
    "meaning": "enclosure"
  },
  {
    "kanji": "郡",
    "meaning": "county"
  },
  {
    "kanji": "郊",
    "meaning": "outskirts"
  },
  {
    "kanji": "部",
    "meaning": "section"
  },
  {
    "kanji": "都",
    "meaning": "metropolis"
  },
  {
    "kanji": "郵",
    "meaning": "mail"
  },
  {
    "kanji": "邦",
    "meaning": "home country"
  },
  {
    "kanji": "郷",
    "meaning": "home town"
  },
  {
    "kanji": "響",
    "meaning": "echo"
  },
  {
    "kanji": "郎",
    "meaning": "son"
  },
  {
    "kanji": "廊",
    "meaning": "corridor"
  },
  {
    "kanji": "盾",
    "meaning": "shield"
  },
  {
    "kanji": "循",
    "meaning": "sequential"
  },
  {
    "kanji": "派",
    "meaning": "faction"
  },
  {
    "kanji": "脈",
    "meaning": "vein"
  },
  {
    "kanji": "衆",
    "meaning": "masses"
  },
  {
    "kanji": "逓",
    "meaning": "parcel post"
  },
  {
    "kanji": "段",
    "meaning": "grade"
  },
  {
    "kanji": "鍛",
    "meaning": "forge"
  },
  {
    "kanji": "后",
    "meaning": "empress"
  },
  {
    "kanji": "幻",
    "meaning": "phantasm"
  },
  {
    "kanji": "司",
    "meaning": "director"
  },
  {
    "kanji": "伺",
    "meaning": "pay respects"
  },
  {
    "kanji": "詞",
    "meaning": "parts of speech"
  },
  {
    "kanji": "飼",
    "meaning": "domesticate"
  },
  {
    "kanji": "嗣",
    "meaning": "heir"
  },
  {
    "kanji": "舟",
    "meaning": "boat"
  },
  {
    "kanji": "舶",
    "meaning": "liner"
  },
  {
    "kanji": "航",
    "meaning": "navigate"
  },
  {
    "kanji": "般",
    "meaning": "carrier"
  },
  {
    "kanji": "盤",
    "meaning": "tray"
  },
  {
    "kanji": "搬",
    "meaning": "conveyor"
  },
  {
    "kanji": "船",
    "meaning": "ship"
  },
  {
    "kanji": "艦",
    "meaning": "warship"
  },
  {
    "kanji": "艇",
    "meaning": "rowboat"
  },
  {
    "kanji": "瓜",
    "meaning": "melon"
  },
  {
    "kanji": "弧",
    "meaning": "arc"
  },
  {
    "kanji": "孤",
    "meaning": "orphan"
  },
  {
    "kanji": "繭",
    "meaning": "cocoon"
  },
  {
    "kanji": "益",
    "meaning": "benefit"
  },
  {
    "kanji": "暇",
    "meaning": "spare time"
  },
  {
    "kanji": "敷",
    "meaning": "spread"
  },
  {
    "kanji": "来",
    "meaning": "come"
  },
  {
    "kanji": "気",
    "meaning": "spirit"
  },
  {
    "kanji": "汽",
    "meaning": "vapor"
  },
  {
    "kanji": "飛",
    "meaning": "fly"
  },
  {
    "kanji": "沈",
    "meaning": "sink"
  },
  {
    "kanji": "妻",
    "meaning": "wife"
  },
  {
    "kanji": "衰",
    "meaning": "decline"
  },
  {
    "kanji": "衷",
    "meaning": "inmost"
  },
  {
    "kanji": "面",
    "meaning": "mask"
  },
  {
    "kanji": "革",
    "meaning": "leather"
  },
  {
    "kanji": "靴",
    "meaning": "shoes"
  },
  {
    "kanji": "覇",
    "meaning": "hegemony"
  },
  {
    "kanji": "声",
    "meaning": "voice"
  },
  {
    "kanji": "呉",
    "meaning": "give"
  },
  {
    "kanji": "娯",
    "meaning": "recreation"
  },
  {
    "kanji": "誤",
    "meaning": "mistake"
  },
  {
    "kanji": "蒸",
    "meaning": "steam"
  },
  {
    "kanji": "承",
    "meaning": "acquiesce"
  },
  {
    "kanji": "函",
    "meaning": "bin"
  },
  {
    "kanji": "極",
    "meaning": "poles"
  },
  {
    "kanji": "牙",
    "meaning": "tusk"
  },
  {
    "kanji": "芽",
    "meaning": "bud"
  },
  {
    "kanji": "邪",
    "meaning": "wicked"
  },
  {
    "kanji": "雅",
    "meaning": "gracious"
  },
  {
    "kanji": "釈",
    "meaning": "explanation/interpretation"
  },
  {
    "kanji": "番",
    "meaning": "turn"
  },
  {
    "kanji": "審",
    "meaning": "hearing"
  },
  {
    "kanji": "翻",
    "meaning": "flip"
  },
  {
    "kanji": "藩",
    "meaning": "clan"
  },
  {
    "kanji": "毛",
    "meaning": "fur"
  },
  {
    "kanji": "耗",
    "meaning": "decrease"
  },
  {
    "kanji": "尾",
    "meaning": "tail"
  },
  {
    "kanji": "宅",
    "meaning": "home"
  },
  {
    "kanji": "託",
    "meaning": "consign"
  },
  {
    "kanji": "為",
    "meaning": "do"
  },
  {
    "kanji": "偽",
    "meaning": "falsehood"
  },
  {
    "kanji": "長",
    "meaning": "long"
  },
  {
    "kanji": "張",
    "meaning": "lengthen"
  },
  {
    "kanji": "帳",
    "meaning": "notebook"
  },
  {
    "kanji": "脹",
    "meaning": "dilate"
  },
  {
    "kanji": "髪",
    "meaning": "hair of the head"
  },
  {
    "kanji": "展",
    "meaning": "unfold"
  },
  {
    "kanji": "喪",
    "meaning": "miss"
  },
  {
    "kanji": "巣",
    "meaning": "nest"
  },
  {
    "kanji": "単",
    "meaning": "simple"
  },
  {
    "kanji": "戦",
    "meaning": "war"
  },
  {
    "kanji": "禅",
    "meaning": "Zen"
  },
  {
    "kanji": "弾",
    "meaning": "bullet"
  },
  {
    "kanji": "桜",
    "meaning": "cherry tree"
  },
  {
    "kanji": "獣",
    "meaning": "animal"
  },
  {
    "kanji": "脳",
    "meaning": "brain"
  },
  {
    "kanji": "悩",
    "meaning": "trouble"
  },
  {
    "kanji": "厳",
    "meaning": "stern"
  },
  {
    "kanji": "鎖",
    "meaning": "chain"
  },
  {
    "kanji": "挙",
    "meaning": "raise"
  },
  {
    "kanji": "誉",
    "meaning": "reputation"
  },
  {
    "kanji": "猟",
    "meaning": "game-hunting"
  },
  {
    "kanji": "鳥",
    "meaning": "bird"
  },
  {
    "kanji": "鳴",
    "meaning": "chirp"
  },
  {
    "kanji": "鶴",
    "meaning": "crane"
  },
  {
    "kanji": "烏",
    "meaning": "crow"
  },
  {
    "kanji": "蔦",
    "meaning": "vine"
  },
  {
    "kanji": "鳩",
    "meaning": "pigeon"
  },
  {
    "kanji": "鶏",
    "meaning": "chicken"
  },
  {
    "kanji": "島",
    "meaning": "island"
  },
  {
    "kanji": "暖",
    "meaning": "warmth"
  },
  {
    "kanji": "媛",
    "meaning": "beautiful woman"
  },
  {
    "kanji": "援",
    "meaning": "abet"
  },
  {
    "kanji": "緩",
    "meaning": "slacken"
  },
  {
    "kanji": "属",
    "meaning": "belong"
  },
  {
    "kanji": "嘱",
    "meaning": "entrust"
  },
  {
    "kanji": "偶",
    "meaning": "accidentally"
  },
  {
    "kanji": "遇",
    "meaning": "interview"
  },
  {
    "kanji": "愚",
    "meaning": "foolish"
  },
  {
    "kanji": "隅",
    "meaning": "corner"
  },
  {
    "kanji": "逆",
    "meaning": "inverted"
  },
  {
    "kanji": "塑",
    "meaning": "model"
  },
  {
    "kanji": "岡",
    "meaning": "Mount"
  },
  {
    "kanji": "鋼",
    "meaning": "steel"
  },
  {
    "kanji": "綱",
    "meaning": "hawser"
  },
  {
    "kanji": "剛",
    "meaning": "sturdy"
  },
  {
    "kanji": "缶",
    "meaning": "tin can"
  },
  {
    "kanji": "陶",
    "meaning": "pottery"
  },
  {
    "kanji": "揺",
    "meaning": "swing"
  },
  {
    "kanji": "謡",
    "meaning": "Noh chanting"
  },
  {
    "kanji": "就",
    "meaning": "concerning"
  },
  {
    "kanji": "懇",
    "meaning": "sociable"
  },
  {
    "kanji": "墾",
    "meaning": "groundbreaking"
  },
  {
    "kanji": "免",
    "meaning": "excuse"
  },
  {
    "kanji": "逸",
    "meaning": "deviate/elude"
  },
  {
    "kanji": "晩",
    "meaning": "nightfall"
  },
  {
    "kanji": "勉",
    "meaning": "exertion"
  },
  {
    "kanji": "象",
    "meaning": "elephant"
  },
  {
    "kanji": "像",
    "meaning": "statue"
  },
  {
    "kanji": "馬",
    "meaning": "horse"
  },
  {
    "kanji": "駒",
    "meaning": "pony"
  },
  {
    "kanji": "験",
    "meaning": "verification"
  },
  {
    "kanji": "騎",
    "meaning": "equestrian"
  },
  {
    "kanji": "駐",
    "meaning": "stop-over/parking"
  },
  {
    "kanji": "駆",
    "meaning": "drive"
  },
  {
    "kanji": "駅",
    "meaning": "station"
  },
  {
    "kanji": "騒",
    "meaning": "boisterous"
  },
  {
    "kanji": "駄",
    "meaning": "burdensome"
  },
  {
    "kanji": "驚",
    "meaning": "wonder"
  },
  {
    "kanji": "篤",
    "meaning": "fervent"
  },
  {
    "kanji": "騰",
    "meaning": "inflation"
  },
  {
    "kanji": "虎",
    "meaning": "tiger"
  },
  {
    "kanji": "虜",
    "meaning": "captive"
  },
  {
    "kanji": "膚",
    "meaning": "skin"
  },
  {
    "kanji": "虚",
    "meaning": "void"
  },
  {
    "kanji": "戯",
    "meaning": "frolic"
  },
  {
    "kanji": "虞",
    "meaning": "uneasiness"
  },
  {
    "kanji": "慮",
    "meaning": "prudence"
  },
  {
    "kanji": "劇",
    "meaning": "drama"
  },
  {
    "kanji": "虐",
    "meaning": "tyrannize"
  },
  {
    "kanji": "鹿",
    "meaning": "deer"
  },
  {
    "kanji": "薦",
    "meaning": "recommend"
  },
  {
    "kanji": "慶",
    "meaning": "jubilation"
  },
  {
    "kanji": "麗",
    "meaning": "lovely"
  },
  {
    "kanji": "熊",
    "meaning": "bear"
  },
  {
    "kanji": "能",
    "meaning": "ability"
  },
  {
    "kanji": "態",
    "meaning": "attitude"
  },
  {
    "kanji": "寅",
    "meaning": "sign of the tiger"
  },
  {
    "kanji": "演",
    "meaning": "performance"
  },
  {
    "kanji": "辰",
    "meaning": "sign of the dragon"
  },
  {
    "kanji": "辱",
    "meaning": "embarrass"
  },
  {
    "kanji": "震",
    "meaning": "quake"
  },
  {
    "kanji": "振",
    "meaning": "shake"
  },
  {
    "kanji": "娠",
    "meaning": "with child"
  },
  {
    "kanji": "唇",
    "meaning": "lips"
  },
  {
    "kanji": "農",
    "meaning": "agriculture"
  },
  {
    "kanji": "濃",
    "meaning": "concentrated"
  },
  {
    "kanji": "送",
    "meaning": "escort/send off"
  },
  {
    "kanji": "関",
    "meaning": "connection"
  },
  {
    "kanji": "咲",
    "meaning": "blossom"
  },
  {
    "kanji": "鬼",
    "meaning": "ghost"
  },
  {
    "kanji": "醜",
    "meaning": "ugly"
  },
  {
    "kanji": "魂",
    "meaning": "soul"
  },
  {
    "kanji": "魔",
    "meaning": "witch"
  },
  {
    "kanji": "魅",
    "meaning": "fascination"
  },
  {
    "kanji": "塊",
    "meaning": "clod"
  },
  {
    "kanji": "襲",
    "meaning": "attack"
  },
  {
    "kanji": "嚇",
    "meaning": "menacing/upbraid"
  },
  {
    "kanji": "朕",
    "meaning": "majestic plural"
  },
  {
    "kanji": "雰",
    "meaning": "atmosphere"
  },
  {
    "kanji": "箇",
    "meaning": "item"
  },
  {
    "kanji": "錬",
    "meaning": "tempering"
  },
  {
    "kanji": "遵",
    "meaning": "abide by"
  },
  {
    "kanji": "罷",
    "meaning": "quit"
  },
  {
    "kanji": "屯",
    "meaning": "barracks"
  },
  {
    "kanji": "且",
    "meaning": "moreover"
  },
  {
    "kanji": "藻",
    "meaning": "seaweed"
  },
  {
    "kanji": "隷",
    "meaning": "slave"
  },
  {
    "kanji": "癒",
    "meaning": "healing"
  },
  {
    "kanji": "丹",
    "meaning": "rust-colored/cinnabar"
  },
  {
    "kanji": "潟",
    "meaning": "lagoon"
  },
  {
    "kanji": "丑",
    "meaning": "sign of the cow"
  },
  {
    "kanji": "卯",
    "meaning": "sign of the hare"
  },
  {
    "kanji": "巳",
    "meaning": "sign of the snake"
  },
  {
    "kanji": "此",
    "meaning": "this here"
  },
  {
    "kanji": "柴",
    "meaning": "brushwood"
  },
  {
    "kanji": "砦",
    "meaning": "fort"
  },
  {
    "kanji": "些",
    "meaning": "whit"
  },
  {
    "kanji": "髭",
    "meaning": "beard"
  },
  {
    "kanji": "璃",
    "meaning": "crystal"
  },
  {
    "kanji": "禽",
    "meaning": "fowl"
  },
  {
    "kanji": "檎",
    "meaning": "apple"
  },
  {
    "kanji": "憐",
    "meaning": "sympathize with"
  },
  {
    "kanji": "燐",
    "meaning": "phosphorus"
  },
  {
    "kanji": "麟",
    "meaning": "camelopard"
  },
  {
    "kanji": "鱗",
    "meaning": "scaled"
  },
  {
    "kanji": "奄",
    "meaning": "encompassing"
  },
  {
    "kanji": "庵",
    "meaning": "hermitage"
  },
  {
    "kanji": "掩",
    "meaning": "shrouded"
  },
  {
    "kanji": "俺",
    "meaning": "myself"
  },
  {
    "kanji": "悛",
    "meaning": "make amends"
  },
  {
    "kanji": "駿",
    "meaning": "steed"
  },
  {
    "kanji": "峻",
    "meaning": "steep"
  },
  {
    "kanji": "竣",
    "meaning": "complete a job"
  },
  {
    "kanji": "臼",
    "meaning": "mortar"
  },
  {
    "kanji": "舅",
    "meaning": "father-in-law"
  },
  {
    "kanji": "鼠",
    "meaning": "mouse"
  },
  {
    "kanji": "鑿",
    "meaning": "bore"
  },
  {
    "kanji": "毀",
    "meaning": "break"
  },
  {
    "kanji": "艘",
    "meaning": "small craft"
  },
  {
    "kanji": "犀",
    "meaning": "rhinoceros"
  },
  {
    "kanji": "皐",
    "meaning": "lunar month"
  },
  {
    "kanji": "脊",
    "meaning": "spinal column"
  },
  {
    "kanji": "畷",
    "meaning": "rice-field footpath"
  },
  {
    "kanji": "綴",
    "meaning": "mend"
  },
  {
    "kanji": "爾",
    "meaning": "let it be"
  },
  {
    "kanji": "璽",
    "meaning": "imperial seal"
  },
  {
    "kanji": "鎧",
    "meaning": "suit of armor"
  },
  {
    "kanji": "凱",
    "meaning": "triumph"
  },
  {
    "kanji": "妖",
    "meaning": "bewitched"
  },
  {
    "kanji": "沃",
    "meaning": "irrigate"
  },
  {
    "kanji": "呑",
    "meaning": "quaff"
  },
  {
    "kanji": "韮",
    "meaning": "leek"
  },
  {
    "kanji": "籤",
    "meaning": "lottery"
  },
  {
    "kanji": "懺",
    "meaning": "penitential"
  },
  {
    "kanji": "芻",
    "meaning": "hay"
  },
  {
    "kanji": "雛",
    "meaning": "chick"
  },
  {
    "kanji": "趨",
    "meaning": "scurry"
  },
  {
    "kanji": "尤",
    "meaning": "understandably"
  },
  {
    "kanji": "稽",
    "meaning": "training"
  },
  {
    "kanji": "厖",
    "meaning": "immense"
  },
  {
    "kanji": "采",
    "meaning": "grab"
  },
  {
    "kanji": "或",
    "meaning": "a"
  },
  {
    "kanji": "斬",
    "meaning": "chop off"
  },
  {
    "kanji": "兎",
    "meaning": "rabbit"
  },
  {
    "kanji": "也",
    "meaning": "est"
  },
  {
    "kanji": "尭",
    "meaning": "lofty"
  },
  {
    "kanji": "巴",
    "meaning": "comma-design"
  },
  {
    "kanji": "甫",
    "meaning": "offspring"
  },
  {
    "kanji": "疋",
    "meaning": "critters"
  },
  {
    "kanji": "菫",
    "meaning": "violet"
  },
  {
    "kanji": "曼",
    "meaning": "mandala"
  },
  {
    "kanji": "巾",
    "meaning": "towel"
  },
  {
    "kanji": "云",
    "meaning": "quote"
  },
  {
    "kanji": "卜",
    "meaning": "augury"
  },
  {
    "kanji": "喬",
    "meaning": "heaven-high"
  },
  {
    "kanji": "莫",
    "meaning": "shalt"
  },
  {
    "kanji": "倭",
    "meaning": "Yamato"
  },
  {
    "kanji": "侠",
    "meaning": "chivalry"
  },
  {
    "kanji": "倦",
    "meaning": "fed up"
  },
  {
    "kanji": "佼",
    "meaning": "comely"
  },
  {
    "kanji": "俄",
    "meaning": "abrupt"
  },
  {
    "kanji": "佃",
    "meaning": "work a field"
  },
  {
    "kanji": "伶",
    "meaning": "minstrel"
  },
  {
    "kanji": "仔",
    "meaning": "animal offspring"
  },
  {
    "kanji": "仇",
    "meaning": "foe"
  },
  {
    "kanji": "伽",
    "meaning": "look after"
  },
  {
    "kanji": "僅",
    "meaning": "trifle"
  },
  {
    "kanji": "僻",
    "meaning": "biased"
  },
  {
    "kanji": "儲",
    "meaning": "make a profit"
  },
  {
    "kanji": "倖",
    "meaning": "bliss"
  },
  {
    "kanji": "僑",
    "meaning": "emigrant"
  },
  {
    "kanji": "侶",
    "meaning": "partner"
  },
  {
    "kanji": "伎",
    "meaning": "performing artist"
  },
  {
    "kanji": "侃",
    "meaning": "integrity"
  },
  {
    "kanji": "倶",
    "meaning": "mate"
  },
  {
    "kanji": "侭",
    "meaning": "as is"
  },
  {
    "kanji": "佑",
    "meaning": "adjutant"
  },
  {
    "kanji": "俣",
    "meaning": "fork in a road"
  },
  {
    "kanji": "傭",
    "meaning": "hire"
  },
  {
    "kanji": "偲",
    "meaning": "memorial"
  },
  {
    "kanji": "脩",
    "meaning": "dried meat"
  },
  {
    "kanji": "倅",
    "meaning": "my son"
  },
  {
    "kanji": "做",
    "meaning": "make do"
  },
  {
    "kanji": "凄",
    "meaning": "nifty"
  },
  {
    "kanji": "冴",
    "meaning": "sharp"
  },
  {
    "kanji": "凋",
    "meaning": "wilt"
  },
  {
    "kanji": "凌",
    "meaning": "pull through"
  },
  {
    "kanji": "冶",
    "meaning": "metallurgy"
  },
  {
    "kanji": "凛",
    "meaning": "stately"
  },
  {
    "kanji": "凧",
    "meaning": "kite"
  },
  {
    "kanji": "凪",
    "meaning": "lull"
  },
  {
    "kanji": "夙",
    "meaning": "earlybird"
  },
  {
    "kanji": "鳳",
    "meaning": "phoenix"
  },
  {
    "kanji": "劉",
    "meaning": "slaughter"
  },
  {
    "kanji": "刹",
    "meaning": "moment"
  },
  {
    "kanji": "剥",
    "meaning": "peel off"
  },
  {
    "kanji": "剃",
    "meaning": "shave"
  },
  {
    "kanji": "匂",
    "meaning": "aroma"
  },
  {
    "kanji": "勾",
    "meaning": "flexed"
  },
  {
    "kanji": "厭",
    "meaning": "despondent"
  },
  {
    "kanji": "雁",
    "meaning": "wild goose"
  },
  {
    "kanji": "贋",
    "meaning": "counterfeit"
  },
  {
    "kanji": "厨",
    "meaning": "kitchen"
  },
  {
    "kanji": "仄",
    "meaning": "insinuate"
  },
  {
    "kanji": "哨",
    "meaning": "scout"
  },
  {
    "kanji": "嘲",
    "meaning": "derision"
  },
  {
    "kanji": "咎",
    "meaning": "reprehend"
  },
  {
    "kanji": "囁",
    "meaning": "whisper"
  },
  {
    "kanji": "喋",
    "meaning": "chatter"
  },
  {
    "kanji": "咽",
    "meaning": "windpipe"
  },
  {
    "kanji": "嘩",
    "meaning": "quarrel"
  },
  {
    "kanji": "噂",
    "meaning": "gossip"
  },
  {
    "kanji": "咳",
    "meaning": "cough"
  },
  {
    "kanji": "喧",
    "meaning": "clamor"
  },
  {
    "kanji": "喉",
    "meaning": "throat"
  },
  {
    "kanji": "唾",
    "meaning": "saliva"
  },
  {
    "kanji": "叩",
    "meaning": "bash"
  },
  {
    "kanji": "嘘",
    "meaning": "fib"
  },
  {
    "kanji": "啄",
    "meaning": "peck at"
  },
  {
    "kanji": "呪",
    "meaning": "curse"
  },
  {
    "kanji": "吠",
    "meaning": "barking"
  },
  {
    "kanji": "吊",
    "meaning": "dangle"
  },
  {
    "kanji": "噛",
    "meaning": "chew"
  },
  {
    "kanji": "叶",
    "meaning": "within my ability"
  },
  {
    "kanji": "吻",
    "meaning": "sides of the mouth"
  },
  {
    "kanji": "吃",
    "meaning": "stammer"
  },
  {
    "kanji": "噺",
    "meaning": "spin a tale"
  },
  {
    "kanji": "噌",
    "meaning": "miso"
  },
  {
    "kanji": "唄",
    "meaning": "pop song"
  },
  {
    "kanji": "叱",
    "meaning": "scold"
  },
  {
    "kanji": "邑",
    "meaning": "city walls"
  },
  {
    "kanji": "呆",
    "meaning": "dumbfounded"
  },
  {
    "kanji": "喰",
    "meaning": "ingest"
  },
  {
    "kanji": "埴",
    "meaning": "clay"
  },
  {
    "kanji": "坤",
    "meaning": "authochthonous"
  },
  {
    "kanji": "堆",
    "meaning": "piled high"
  },
  {
    "kanji": "壕",
    "meaning": "dugout"
  },
  {
    "kanji": "垢",
    "meaning": "blemish"
  },
  {
    "kanji": "坦",
    "meaning": "flat"
  },
  {
    "kanji": "埠",
    "meaning": "wharf"
  },
  {
    "kanji": "填",
    "meaning": "stuff up"
  },
  {
    "kanji": "堰",
    "meaning": "dam"
  },
  {
    "kanji": "堵",
    "meaning": "railing"
  },
  {
    "kanji": "嬰",
    "meaning": "suckling infant"
  },
  {
    "kanji": "姦",
    "meaning": "violate"
  },
  {
    "kanji": "妬",
    "meaning": "jealous"
  },
  {
    "kanji": "婢",
    "meaning": "handmaiden"
  },
  {
    "kanji": "婉",
    "meaning": "well finished"
  },
  {
    "kanji": "娼",
    "meaning": "harlot"
  },
  {
    "kanji": "妓",
    "meaning": "courtesan"
  },
  {
    "kanji": "娃",
    "meaning": "fair"
  },
  {
    "kanji": "姪",
    "meaning": "niece"
  },
  {
    "kanji": "嫉",
    "meaning": "envy"
  },
  {
    "kanji": "嬬",
    "meaning": "mistress"
  },
  {
    "kanji": "姥",
    "meaning": "aged woman"
  },
  {
    "kanji": "姑",
    "meaning": "mother-in-law"
  },
  {
    "kanji": "姐",
    "meaning": "young miss"
  },
  {
    "kanji": "嬉",
    "meaning": "overjoyed"
  },
  {
    "kanji": "孕",
    "meaning": "expecting"
  },
  {
    "kanji": "孜",
    "meaning": "assiduous"
  },
  {
    "kanji": "宥",
    "meaning": "soothe"
  },
  {
    "kanji": "寓",
    "meaning": "imply"
  },
  {
    "kanji": "宏",
    "meaning": "extensive"
  },
  {
    "kanji": "牢",
    "meaning": "jail"
  },
  {
    "kanji": "塞",
    "meaning": "block up"
  },
  {
    "kanji": "宋",
    "meaning": "Sung dynasty"
  },
  {
    "kanji": "宍",
    "meaning": "venison"
  },
  {
    "kanji": "屠",
    "meaning": "butchering"
  },
  {
    "kanji": "屁",
    "meaning": "fart"
  },
  {
    "kanji": "屑",
    "meaning": "rubbish"
  },
  {
    "kanji": "尻",
    "meaning": "buttocks"
  },
  {
    "kanji": "屡",
    "meaning": "frequently"
  },
  {
    "kanji": "屍",
    "meaning": "corpse"
  },
  {
    "kanji": "屏",
    "meaning": "folding screen"
  },
  {
    "kanji": "嵩",
    "meaning": "high-reaching"
  },
  {
    "kanji": "崚",
    "meaning": "rugged mountains"
  },
  {
    "kanji": "峨",
    "meaning": "high mountain"
  },
  {
    "kanji": "崖",
    "meaning": "bluffs"
  },
  {
    "kanji": "嶺",
    "meaning": "mountaintop"
  },
  {
    "kanji": "嵌",
    "meaning": "fit into"
  },
  {
    "kanji": "嵯",
    "meaning": "rocky"
  },
  {
    "kanji": "帖",
    "meaning": "quire"
  },
  {
    "kanji": "幡",
    "meaning": "banner"
  },
  {
    "kanji": "幟",
    "meaning": "pennant"
  },
  {
    "kanji": "庖",
    "meaning": "cleaver"
  },
  {
    "kanji": "廓",
    "meaning": "licensed quarters"
  },
  {
    "kanji": "庇",
    "meaning": "overhang"
  },
  {
    "kanji": "鷹",
    "meaning": "hawk"
  },
  {
    "kanji": "庄",
    "meaning": "shire"
  },
  {
    "kanji": "廟",
    "meaning": "tomb sanctuary"
  },
  {
    "kanji": "彊",
    "meaning": "strengthen"
  },
  {
    "kanji": "弥",
    "meaning": "more and more"
  },
  {
    "kanji": "弛",
    "meaning": "loosen"
  },
  {
    "kanji": "粥",
    "meaning": "rice gruel"
  },
  {
    "kanji": "挽",
    "meaning": "lathe"
  },
  {
    "kanji": "撞",
    "meaning": "bump into"
  },
  {
    "kanji": "扮",
    "meaning": "disguise"
  },
  {
    "kanji": "掠",
    "meaning": "pillage"
  },
  {
    "kanji": "挨",
    "meaning": "shove"
  },
  {
    "kanji": "掴",
    "meaning": "clutch"
  },
  {
    "kanji": "捺",
    "meaning": "impress"
  },
  {
    "kanji": "捻",
    "meaning": "wrenching"
  },
  {
    "kanji": "掻",
    "meaning": "scratch"
  },
  {
    "kanji": "撰",
    "meaning": "assortment"
  },
  {
    "kanji": "拭",
    "meaning": "wipe"
  },
  {
    "kanji": "揃",
    "meaning": "muster"
  },
  {
    "kanji": "捌",
    "meaning": "deal with"
  },
  {
    "kanji": "撹",
    "meaning": "churn up"
  },
  {
    "kanji": "摺",
    "meaning": "rubbing"
  },
  {
    "kanji": "按",
    "meaning": "press down on"
  },
  {
    "kanji": "捉",
    "meaning": "nab"
  },
  {
    "kanji": "拶",
    "meaning": "imminent"
  },
  {
    "kanji": "播",
    "meaning": "disseminate"
  },
  {
    "kanji": "揖",
    "meaning": "interpretation"
  },
  {
    "kanji": "托",
    "meaning": "receptable"
  },
  {
    "kanji": "捧",
    "meaning": "dedicate"
  },
  {
    "kanji": "撚",
    "meaning": "twirl"
  },
  {
    "kanji": "挺",
    "meaning": "counter for tools"
  },
  {
    "kanji": "擾",
    "meaning": "commotion"
  },
  {
    "kanji": "捗",
    "meaning": "make headway"
  },
  {
    "kanji": "撫",
    "meaning": "petting"
  },
  {
    "kanji": "撒",
    "meaning": "sprinkle"
  },
  {
    "kanji": "擢",
    "meaning": "outstanding"
  },
  {
    "kanji": "捷",
    "meaning": "spoils"
  },
  {
    "kanji": "抉",
    "meaning": "gouge out"
  },
  {
    "kanji": "怯",
    "meaning": "wince"
  },
  {
    "kanji": "惟",
    "meaning": "ponder"
  },
  {
    "kanji": "惚",
    "meaning": "infatuation"
  },
  {
    "kanji": "怜",
    "meaning": "quickwitted"
  },
  {
    "kanji": "惇",
    "meaning": "considerate"
  },
  {
    "kanji": "憧",
    "meaning": "yearn"
  },
  {
    "kanji": "恰",
    "meaning": "as if"
  },
  {
    "kanji": "恢",
    "meaning": "enlarge"
  },
  {
    "kanji": "悌",
    "meaning": "respect for elders"
  },
  {
    "kanji": "湧",
    "meaning": "bubble up"
  },
  {
    "kanji": "澪",
    "meaning": "canal"
  },
  {
    "kanji": "洸",
    "meaning": "glistening"
  },
  {
    "kanji": "滉",
    "meaning": "bounding main"
  },
  {
    "kanji": "漱",
    "meaning": "gargle"
  },
  {
    "kanji": "洲",
    "meaning": "continent"
  },
  {
    "kanji": "洵",
    "meaning": "swirling waters"
  },
  {
    "kanji": "滲",
    "meaning": "seep"
  },
  {
    "kanji": "洒",
    "meaning": "rinse"
  },
  {
    "kanji": "沐",
    "meaning": "douse"
  },
  {
    "kanji": "泪",
    "meaning": "teardrops"
  },
  {
    "kanji": "渾",
    "meaning": "gushing"
  },
  {
    "kanji": "沙",
    "meaning": "grains of sand"
  },
  {
    "kanji": "涜",
    "meaning": "blaspheme"
  },
  {
    "kanji": "淫",
    "meaning": "lewd"
  },
  {
    "kanji": "梁",
    "meaning": "roofbeam"
  },
  {
    "kanji": "澱",
    "meaning": "sediment"
  },
  {
    "kanji": "氾",
    "meaning": "widespread"
  },
  {
    "kanji": "洛",
    "meaning": "old Kyoto"
  },
  {
    "kanji": "汝",
    "meaning": "thou"
  },
  {
    "kanji": "漉",
    "meaning": "filter"
  },
  {
    "kanji": "瀕",
    "meaning": "on the verge of"
  },
  {
    "kanji": "濠",
    "meaning": "moat"
  },
  {
    "kanji": "溌",
    "meaning": "spray"
  },
  {
    "kanji": "溺",
    "meaning": "drowning"
  },
  {
    "kanji": "湊",
    "meaning": "port"
  },
  {
    "kanji": "淋",
    "meaning": "solitude"
  },
  {
    "kanji": "浩",
    "meaning": "abounding"
  },
  {
    "kanji": "汀",
    "meaning": "water's edge"
  },
  {
    "kanji": "鴻",
    "meaning": "large goose"
  },
  {
    "kanji": "潅",
    "meaning": "souse"
  },
  {
    "kanji": "溢",
    "meaning": "brimming"
  },
  {
    "kanji": "汰",
    "meaning": "cleanse"
  },
  {
    "kanji": "湛",
    "meaning": "inundate"
  },
  {
    "kanji": "淳",
    "meaning": "immaculate"
  },
  {
    "kanji": "潰",
    "meaning": "defile"
  },
  {
    "kanji": "渥",
    "meaning": "moisten"
  },
  {
    "kanji": "灘",
    "meaning": "rough seas"
  },
  {
    "kanji": "汲",
    "meaning": "draw water"
  },
  {
    "kanji": "瀞",
    "meaning": "river pool"
  },
  {
    "kanji": "溜",
    "meaning": "cumulation"
  },
  {
    "kanji": "渕",
    "meaning": "abyss"
  },
  {
    "kanji": "沌",
    "meaning": "chaos"
  },
  {
    "kanji": "汎",
    "meaning": "pan"
  },
  {
    "kanji": "濾",
    "meaning": "strainer"
  },
  {
    "kanji": "濡",
    "meaning": "drench"
  },
  {
    "kanji": "淀",
    "meaning": "eddy"
  },
  {
    "kanji": "涅",
    "meaning": "fabrication"
  },
  {
    "kanji": "釜",
    "meaning": "cauldron"
  },
  {
    "kanji": "斧",
    "meaning": "hatchet"
  },
  {
    "kanji": "爺",
    "meaning": "grandpa"
  },
  {
    "kanji": "猾",
    "meaning": "sly"
  },
  {
    "kanji": "猥",
    "meaning": "indecent"
  },
  {
    "kanji": "狡",
    "meaning": "cunning"
  },
  {
    "kanji": "狸",
    "meaning": "racoon dog"
  },
  {
    "kanji": "狼",
    "meaning": "wolf"
  },
  {
    "kanji": "狽",
    "meaning": "flustered"
  },
  {
    "kanji": "狗",
    "meaning": "pup"
  },
  {
    "kanji": "狐",
    "meaning": "fox"
  },
  {
    "kanji": "狛",
    "meaning": "a-un"
  },
  {
    "kanji": "狙",
    "meaning": "aim at"
  },
  {
    "kanji": "獅",
    "meaning": "lion"
  },
  {
    "kanji": "狒",
    "meaning": "baboon"
  },
  {
    "kanji": "莨",
    "meaning": "tobacco"
  },
  {
    "kanji": "茉",
    "meaning": "jasmine"
  },
  {
    "kanji": "莉",
    "meaning": "hawthorn"
  },
  {
    "kanji": "苺",
    "meaning": "strawberry"
  },
  {
    "kanji": "萩",
    "meaning": "bush clover"
  },
  {
    "kanji": "藝",
    "meaning": "technique [old]"
  },
  {
    "kanji": "薙",
    "meaning": "trim"
  },
  {
    "kanji": "蓑",
    "meaning": "straw raincoat"
  },
  {
    "kanji": "萎",
    "meaning": "numb"
  },
  {
    "kanji": "苔",
    "meaning": "moss"
  },
  {
    "kanji": "蕩",
    "meaning": "prodigal"
  },
  {
    "kanji": "蔽",
    "meaning": "cover over"
  },
  {
    "kanji": "蔓",
    "meaning": "tendril"
  },
  {
    "kanji": "蓮",
    "meaning": "lotus"
  },
  {
    "kanji": "芙",
    "meaning": "lotus flower"
  },
  {
    "kanji": "蓉",
    "meaning": "lotus blossom"
  },
  {
    "kanji": "蘭",
    "meaning": "orchid"
  },
  {
    "kanji": "芦",
    "meaning": "hollow reed"
  },
  {
    "kanji": "薯",
    "meaning": "yam"
  },
  {
    "kanji": "菖",
    "meaning": "iris"
  },
  {
    "kanji": "蕉",
    "meaning": "banana"
  },
  {
    "kanji": "芯",
    "meaning": "wick"
  },
  {
    "kanji": "蕎",
    "meaning": "buckwheat"
  },
  {
    "kanji": "蕗",
    "meaning": "butterbur"
  },
  {
    "kanji": "藍",
    "meaning": "indigo"
  },
  {
    "kanji": "茄",
    "meaning": "eggplant"
  },
  {
    "kanji": "苛",
    "meaning": "bullying"
  },
  {
    "kanji": "蔭",
    "meaning": "behind the scenes"
  },
  {
    "kanji": "蓬",
    "meaning": "wormwood"
  },
  {
    "kanji": "芥",
    "meaning": "mustard"
  },
  {
    "kanji": "萌",
    "meaning": "germinate"
  },
  {
    "kanji": "葡",
    "meaning": "grape"
  },
  {
    "kanji": "萄",
    "meaning": "grape vine"
  },
  {
    "kanji": "蘇",
    "meaning": "resurrect"
  },
  {
    "kanji": "蕃",
    "meaning": "grow wild"
  },
  {
    "kanji": "苓",
    "meaning": "cocklebur"
  },
  {
    "kanji": "菰",
    "meaning": "rush mat"
  },
  {
    "kanji": "蒙",
    "meaning": "darken"
  },
  {
    "kanji": "茅",
    "meaning": "grassy reed"
  },
  {
    "kanji": "芭",
    "meaning": "plantain"
  },
  {
    "kanji": "苅",
    "meaning": "mow"
  },
  {
    "kanji": "蓋",
    "meaning": "lid"
  },
  {
    "kanji": "葱",
    "meaning": "onion"
  },
  {
    "kanji": "蔑",
    "meaning": "revile"
  },
  {
    "kanji": "葵",
    "meaning": "hollyhock"
  },
  {
    "kanji": "葺",
    "meaning": "shingling"
  },
  {
    "kanji": "蕊",
    "meaning": "stamen"
  },
  {
    "kanji": "茸",
    "meaning": "mushroom"
  },
  {
    "kanji": "蒔",
    "meaning": "sowing"
  },
  {
    "kanji": "芹",
    "meaning": "parsley"
  },
  {
    "kanji": "苫",
    "meaning": "thatching"
  },
  {
    "kanji": "葛",
    "meaning": "kudzu"
  },
  {
    "kanji": "蒼",
    "meaning": "pale blue"
  },
  {
    "kanji": "藁",
    "meaning": "straw"
  },
  {
    "kanji": "蕪",
    "meaning": "turnip"
  },
  {
    "kanji": "藷",
    "meaning": "sweet potato"
  },
  {
    "kanji": "薮",
    "meaning": "quack"
  },
  {
    "kanji": "蒜",
    "meaning": "garlic"
  },
  {
    "kanji": "蕨",
    "meaning": "bracken"
  },
  {
    "kanji": "蔚",
    "meaning": "grow plentiful"
  },
  {
    "kanji": "茜",
    "meaning": "madder red"
  },
  {
    "kanji": "莞",
    "meaning": "candle rush"
  },
  {
    "kanji": "蒐",
    "meaning": "collector"
  },
  {
    "kanji": "菅",
    "meaning": "sedge"
  },
  {
    "kanji": "葦",
    "meaning": "ditch reed"
  },
  {
    "kanji": "迪",
    "meaning": "Way"
  },
  {
    "kanji": "辿",
    "meaning": "track down"
  },
  {
    "kanji": "這",
    "meaning": "crawl"
  },
  {
    "kanji": "迂",
    "meaning": "detour"
  },
  {
    "kanji": "遁",
    "meaning": "elude"
  },
  {
    "kanji": "逢",
    "meaning": "tryst"
  },
  {
    "kanji": "遥",
    "meaning": "far off"
  },
  {
    "kanji": "遼",
    "meaning": "remote"
  },
  {
    "kanji": "逼",
    "meaning": "pressing"
  },
  {
    "kanji": "迄",
    "meaning": "until"
  },
  {
    "kanji": "遜",
    "meaning": "modest"
  },
  {
    "kanji": "逗",
    "meaning": "standstill"
  },
  {
    "kanji": "郁",
    "meaning": "cultured"
  },
  {
    "kanji": "鄭",
    "meaning": "courtesy"
  },
  {
    "kanji": "隙",
    "meaning": "chink"
  },
  {
    "kanji": "隈",
    "meaning": "nook"
  },
  {
    "kanji": "憑",
    "meaning": "possessed"
  },
  {
    "kanji": "惹",
    "meaning": "attract"
  },
  {
    "kanji": "悉",
    "meaning": "without exception"
  },
  {
    "kanji": "忽",
    "meaning": "instantaneously"
  },
  {
    "kanji": "惣",
    "meaning": "firstborn son"
  },
  {
    "kanji": "愈",
    "meaning": "in the nick of time"
  },
  {
    "kanji": "恕",
    "meaning": "sensitive"
  },
  {
    "kanji": "昴",
    "meaning": "overarching"
  },
  {
    "kanji": "晋",
    "meaning": "progress"
  },
  {
    "kanji": "曖",
    "meaning": "equivocal"
  },
  {
    "kanji": "晟",
    "meaning": "aglow"
  },
  {
    "kanji": "暈",
    "meaning": "halo"
  },
  {
    "kanji": "暉",
    "meaning": "glitter"
  },
  {
    "kanji": "旱",
    "meaning": "dry weather"
  },
  {
    "kanji": "晏",
    "meaning": "clear skies"
  },
  {
    "kanji": "晨",
    "meaning": "morrow"
  },
  {
    "kanji": "晒",
    "meaning": "bleaching"
  },
  {
    "kanji": "昧",
    "meaning": "obscure"
  },
  {
    "kanji": "晃",
    "meaning": "limpid"
  },
  {
    "kanji": "曝",
    "meaning": "air out"
  },
  {
    "kanji": "曙",
    "meaning": "dawn"
  },
  {
    "kanji": "昂",
    "meaning": "elevate"
  },
  {
    "kanji": "旺",
    "meaning": "effulgent"
  },
  {
    "kanji": "昏",
    "meaning": "dusk"
  },
  {
    "kanji": "晦",
    "meaning": "last day of the month"
  },
  {
    "kanji": "腎",
    "meaning": "kidney"
  },
  {
    "kanji": "股",
    "meaning": "thigh"
  },
  {
    "kanji": "膿",
    "meaning": "pus"
  },
  {
    "kanji": "腑",
    "meaning": "viscera"
  },
  {
    "kanji": "胱",
    "meaning": "bladder"
  },
  {
    "kanji": "胚",
    "meaning": "embryo"
  },
  {
    "kanji": "肛",
    "meaning": "anus"
  },
  {
    "kanji": "臆",
    "meaning": "cowardice"
  },
  {
    "kanji": "膝",
    "meaning": "knee"
  },
  {
    "kanji": "脆",
    "meaning": "fragile"
  },
  {
    "kanji": "肋",
    "meaning": "rib"
  },
  {
    "kanji": "肘",
    "meaning": "elbow"
  },
  {
    "kanji": "腔",
    "meaning": "body cavity"
  },
  {
    "kanji": "腺",
    "meaning": "gland"
  },
  {
    "kanji": "腫",
    "meaning": "tumor"
  },
  {
    "kanji": "膳",
    "meaning": "dining tray"
  },
  {
    "kanji": "肱",
    "meaning": "armrest"
  },
  {
    "kanji": "胡",
    "meaning": "uncivilized"
  },
  {
    "kanji": "楓",
    "meaning": "maple tree"
  },
  {
    "kanji": "枕",
    "meaning": "pillow"
  },
  {
    "kanji": "楊",
    "meaning": "purple willow"
  },
  {
    "kanji": "椋",
    "meaning": "Oriental elm"
  },
  {
    "kanji": "榛",
    "meaning": "hazel"
  },
  {
    "kanji": "櫛",
    "meaning": "comb"
  },
  {
    "kanji": "槌",
    "meaning": "wooden hammer"
  },
  {
    "kanji": "樵",
    "meaning": "mallet"
  },
  {
    "kanji": "梯",
    "meaning": "ladder"
  },
  {
    "kanji": "椅",
    "meaning": "chair"
  },
  {
    "kanji": "柿",
    "meaning": "persimmon"
  },
  {
    "kanji": "柑",
    "meaning": "citrus tree"
  },
  {
    "kanji": "桁",
    "meaning": "girder"
  },
  {
    "kanji": "杭",
    "meaning": "picket"
  },
  {
    "kanji": "柊",
    "meaning": "holly"
  },
  {
    "kanji": "柚",
    "meaning": "citron"
  },
  {
    "kanji": "椀",
    "meaning": "wooden bowl"
  },
  {
    "kanji": "栂",
    "meaning": "hemlock"
  },
  {
    "kanji": "柾",
    "meaning": "spindle tree"
  },
  {
    "kanji": "榊",
    "meaning": "sacred Shinto tree"
  },
  {
    "kanji": "樫",
    "meaning": "evergreen oak"
  },
  {
    "kanji": "槙",
    "meaning": "Chinese black pine"
  },
  {
    "kanji": "楢",
    "meaning": "Japanese oak"
  },
  {
    "kanji": "橘",
    "meaning": "mandarin orange"
  },
  {
    "kanji": "桧",
    "meaning": "Japanese cypress"
  },
  {
    "kanji": "棲",
    "meaning": "roost"
  },
  {
    "kanji": "栖",
    "meaning": "nestle"
  },
  {
    "kanji": "梗",
    "meaning": "spiny"
  },
  {
    "kanji": "桔",
    "meaning": "bellflower"
  },
  {
    "kanji": "杜",
    "meaning": "temple grove"
  },
  {
    "kanji": "杷",
    "meaning": "grain rake"
  },
  {
    "kanji": "梶",
    "meaning": "oar"
  },
  {
    "kanji": "杵",
    "meaning": "wooden pestle"
  },
  {
    "kanji": "杖",
    "meaning": "cane"
  },
  {
    "kanji": "椎",
    "meaning": "sweet oak"
  },
  {
    "kanji": "樽",
    "meaning": "barrel"
  },
  {
    "kanji": "柵",
    "meaning": "palisade"
  },
  {
    "kanji": "櫓",
    "meaning": "turret"
  },
  {
    "kanji": "橿",
    "meaning": "sturdy oak"
  },
  {
    "kanji": "杓",
    "meaning": "wooden ladle"
  },
  {
    "kanji": "李",
    "meaning": "damson"
  },
  {
    "kanji": "棉",
    "meaning": "raw cotton"
  },
  {
    "kanji": "楯",
    "meaning": "escutcheon"
  },
  {
    "kanji": "榎",
    "meaning": "hackberry"
  },
  {
    "kanji": "樺",
    "meaning": "birch"
  },
  {
    "kanji": "槍",
    "meaning": "lance"
  },
  {
    "kanji": "柘",
    "meaning": "wild mulberry"
  },
  {
    "kanji": "梱",
    "meaning": "bale"
  },
  {
    "kanji": "枇",
    "meaning": "loquat"
  },
  {
    "kanji": "樋",
    "meaning": "downspout"
  },
  {
    "kanji": "橇",
    "meaning": "sled"
  },
  {
    "kanji": "槃",
    "meaning": "enjoyment"
  },
  {
    "kanji": "栞",
    "meaning": "bookmark"
  },
  {
    "kanji": "椰",
    "meaning": "coconut tree"
  },
  {
    "kanji": "檀",
    "meaning": "sandalwood"
  },
  {
    "kanji": "樗",
    "meaning": "plotosid"
  },
  {
    "kanji": "槻",
    "meaning": "zelkova"
  },
  {
    "kanji": "椙",
    "meaning": "cryptomeria"
  },
  {
    "kanji": "彬",
    "meaning": "copious"
  },
  {
    "kanji": "桶",
    "meaning": "bucket"
  },
  {
    "kanji": "楕",
    "meaning": "ellipse"
  },
  {
    "kanji": "樒",
    "meaning": "star-anise"
  },
  {
    "kanji": "毬",
    "meaning": "furball"
  },
  {
    "kanji": "燿",
    "meaning": "twinkle"
  },
  {
    "kanji": "燎",
    "meaning": "watchfire"
  },
  {
    "kanji": "炬",
    "meaning": "torch"
  },
  {
    "kanji": "焚",
    "meaning": "kindle"
  },
  {
    "kanji": "灸",
    "meaning": "moxa"
  },
  {
    "kanji": "燭",
    "meaning": "candlelight"
  },
  {
    "kanji": "煽",
    "meaning": "fanning"
  },
  {
    "kanji": "煤",
    "meaning": "soot"
  },
  {
    "kanji": "煉",
    "meaning": "firing"
  },
  {
    "kanji": "燦",
    "meaning": "dazzling"
  },
  {
    "kanji": "灼",
    "meaning": "refulgent"
  },
  {
    "kanji": "烙",
    "meaning": "branding"
  },
  {
    "kanji": "焔",
    "meaning": "flames"
  },
  {
    "kanji": "熔",
    "meaning": "fuse metal"
  },
  {
    "kanji": "煎",
    "meaning": "roast"
  },
  {
    "kanji": "烹",
    "meaning": "stew"
  },
  {
    "kanji": "牽",
    "meaning": "tug"
  },
  {
    "kanji": "牝",
    "meaning": "female animal"
  },
  {
    "kanji": "牡",
    "meaning": "male animal"
  },
  {
    "kanji": "瑶",
    "meaning": "precious stone"
  },
  {
    "kanji": "琳",
    "meaning": "chime"
  },
  {
    "kanji": "瑠",
    "meaning": "marine blue"
  },
  {
    "kanji": "斑",
    "meaning": "speckled"
  },
  {
    "kanji": "琉",
    "meaning": "lapis lazuli"
  },
  {
    "kanji": "弄",
    "meaning": "tinker with"
  },
  {
    "kanji": "瑳",
    "meaning": "burnish"
  },
  {
    "kanji": "琢",
    "meaning": "hone"
  },
  {
    "kanji": "珊",
    "meaning": "coral"
  },
  {
    "kanji": "瑚",
    "meaning": "coral reef"
  },
  {
    "kanji": "瑞",
    "meaning": "fortunate"
  },
  {
    "kanji": "珪",
    "meaning": "silicon"
  },
  {
    "kanji": "玖",
    "meaning": "jet"
  },
  {
    "kanji": "瑛",
    "meaning": "crystal stone"
  },
  {
    "kanji": "玩",
    "meaning": "toy"
  },
  {
    "kanji": "玲",
    "meaning": "tinkling"
  },
  {
    "kanji": "畏",
    "meaning": "apprehensive"
  },
  {
    "kanji": "畢",
    "meaning": "lastly"
  },
  {
    "kanji": "畦",
    "meaning": "paddy-field ridge"
  },
  {
    "kanji": "痒",
    "meaning": "itch"
  },
  {
    "kanji": "痰",
    "meaning": "phlegm"
  },
  {
    "kanji": "疹",
    "meaning": "measles"
  },
  {
    "kanji": "痔",
    "meaning": "hemorrhoids"
  },
  {
    "kanji": "癌",
    "meaning": "cancer"
  },
  {
    "kanji": "痩",
    "meaning": "lose weight"
  },
  {
    "kanji": "痕",
    "meaning": "scar"
  },
  {
    "kanji": "痺",
    "meaning": "paralysis"
  },
  {
    "kanji": "眸",
    "meaning": "apple of the eye"
  },
  {
    "kanji": "眩",
    "meaning": "dizzy"
  },
  {
    "kanji": "瞭",
    "meaning": "obvious"
  },
  {
    "kanji": "眉",
    "meaning": "eyebrow"
  },
  {
    "kanji": "雉",
    "meaning": "pheasant"
  },
  {
    "kanji": "矩",
    "meaning": "carpenter's square"
  },
  {
    "kanji": "磐",
    "meaning": "crag"
  },
  {
    "kanji": "碇",
    "meaning": "grapnel"
  },
  {
    "kanji": "碧",
    "meaning": "blue-green"
  },
  {
    "kanji": "硯",
    "meaning": "inkstone"
  },
  {
    "kanji": "砥",
    "meaning": "grindstone"
  },
  {
    "kanji": "碗",
    "meaning": "teacup"
  },
  {
    "kanji": "碍",
    "meaning": "obstacle"
  },
  {
    "kanji": "碩",
    "meaning": "illustrious"
  },
  {
    "kanji": "磯",
    "meaning": "rocky beach"
  },
  {
    "kanji": "砺",
    "meaning": "whetstone"
  },
  {
    "kanji": "碓",
    "meaning": "mill"
  },
  {
    "kanji": "禦",
    "meaning": "fend off"
  },
  {
    "kanji": "祷",
    "meaning": "beseech"
  },
  {
    "kanji": "祐",
    "meaning": "ancestral tablet"
  },
  {
    "kanji": "祇",
    "meaning": "local god"
  },
  {
    "kanji": "祢",
    "meaning": "ancestral shrine"
  },
  {
    "kanji": "禄",
    "meaning": "salarium"
  },
  {
    "kanji": "禎",
    "meaning": "felicitation"
  },
  {
    "kanji": "秤",
    "meaning": "balancing scales"
  },
  {
    "kanji": "黍",
    "meaning": "millet"
  },
  {
    "kanji": "禿",
    "meaning": "bald"
  },
  {
    "kanji": "稔",
    "meaning": "bear fruit"
  },
  {
    "kanji": "稗",
    "meaning": "crabgrass"
  },
  {
    "kanji": "穣",
    "meaning": "bumper crop"
  },
  {
    "kanji": "稜",
    "meaning": "imperial authority"
  },
  {
    "kanji": "稀",
    "meaning": "sparse"
  },
  {
    "kanji": "穆",
    "meaning": "obeisant"
  },
  {
    "kanji": "窺",
    "meaning": "peep"
  },
  {
    "kanji": "窄",
    "meaning": "tight"
  },
  {
    "kanji": "窟",
    "meaning": "cavern"
  },
  {
    "kanji": "穿",
    "meaning": "drill"
  },
  {
    "kanji": "竃",
    "meaning": "kitchen stove"
  },
  {
    "kanji": "竪",
    "meaning": "longness"
  },
  {
    "kanji": "颯",
    "meaning": "rustling"
  },
  {
    "kanji": "站",
    "meaning": "outpost"
  },
  {
    "kanji": "靖",
    "meaning": "repose"
  },
  {
    "kanji": "妾",
    "meaning": "concubine"
  },
  {
    "kanji": "衿",
    "meaning": "lapel"
  },
  {
    "kanji": "裾",
    "meaning": "hem"
  },
  {
    "kanji": "袷",
    "meaning": "lined kimono"
  },
  {
    "kanji": "袴",
    "meaning": "pleated skirt"
  },
  {
    "kanji": "襖",
    "meaning": "sliding door"
  },
  {
    "kanji": "笙",
    "meaning": "Chinese panpipe"
  },
  {
    "kanji": "筏",
    "meaning": "raft"
  },
  {
    "kanji": "簾",
    "meaning": "bamboo blinds"
  },
  {
    "kanji": "箪",
    "meaning": "rattan box"
  },
  {
    "kanji": "竿",
    "meaning": "pole"
  },
  {
    "kanji": "箆",
    "meaning": "spatula"
  },
  {
    "kanji": "箔",
    "meaning": "foil"
  },
  {
    "kanji": "笥",
    "meaning": "wardrobe"
  },
  {
    "kanji": "箭",
    "meaning": "arrow shaft"
  },
  {
    "kanji": "筑",
    "meaning": "ancient harp"
  },
  {
    "kanji": "篭",
    "meaning": "cage"
  },
  {
    "kanji": "篠",
    "meaning": "slender bamboo"
  },
  {
    "kanji": "箸",
    "meaning": "chopsticks"
  },
  {
    "kanji": "纂",
    "meaning": "redaction"
  },
  {
    "kanji": "竺",
    "meaning": "bamboo cane"
  },
  {
    "kanji": "箕",
    "meaning": "winnowing fan"
  },
  {
    "kanji": "笈",
    "meaning": "backpack"
  },
  {
    "kanji": "篇",
    "meaning": "livraison"
  },
  {
    "kanji": "筈",
    "meaning": "should"
  },
  {
    "kanji": "簸",
    "meaning": "winnow"
  },
  {
    "kanji": "粕",
    "meaning": "settlings"
  },
  {
    "kanji": "糟",
    "meaning": "lees"
  },
  {
    "kanji": "糊",
    "meaning": "paste"
  },
  {
    "kanji": "籾",
    "meaning": "unhulled rice"
  },
  {
    "kanji": "糠",
    "meaning": "rice bran"
  },
  {
    "kanji": "糞",
    "meaning": "excrement"
  },
  {
    "kanji": "粟",
    "meaning": "foxtail millet"
  },
  {
    "kanji": "繋",
    "meaning": "link up"
  },
  {
    "kanji": "綸",
    "meaning": "twine"
  },
  {
    "kanji": "絨",
    "meaning": "carpet yarn"
  },
  {
    "kanji": "絆",
    "meaning": "ties"
  },
  {
    "kanji": "緋",
    "meaning": "scarlet"
  },
  {
    "kanji": "綜",
    "meaning": "synthesis"
  },
  {
    "kanji": "紐",
    "meaning": "string"
  },
  {
    "kanji": "紘",
    "meaning": "chinstrap"
  },
  {
    "kanji": "纏",
    "meaning": "summarize"
  },
  {
    "kanji": "絢",
    "meaning": "gorgeous"
  },
  {
    "kanji": "繍",
    "meaning": "embroidery"
  },
  {
    "kanji": "紬",
    "meaning": "pongee"
  },
  {
    "kanji": "綺",
    "meaning": "ornate"
  },
  {
    "kanji": "綾",
    "meaning": "damask"
  },
  {
    "kanji": "絃",
    "meaning": "catgut"
  },
  {
    "kanji": "綻",
    "meaning": "come apart at the seams"
  },
  {
    "kanji": "縞",
    "meaning": "stripe"
  },
  {
    "kanji": "綬",
    "meaning": "gimp"
  },
  {
    "kanji": "紗",
    "meaning": "gossamer"
  },
  {
    "kanji": "舵",
    "meaning": "rudder"
  },
  {
    "kanji": "舷",
    "meaning": "gunwale"
  },
  {
    "kanji": "聯",
    "meaning": "strung together"
  },
  {
    "kanji": "聡",
    "meaning": "attentive"
  },
  {
    "kanji": "聘",
    "meaning": "summons"
  },
  {
    "kanji": "耽",
    "meaning": "addiction"
  },
  {
    "kanji": "耶",
    "meaning": "exclamation"
  },
  {
    "kanji": "蚤",
    "meaning": "flea"
  },
  {
    "kanji": "蟹",
    "meaning": "crab"
  },
  {
    "kanji": "蛋",
    "meaning": "protein"
  },
  {
    "kanji": "蟄",
    "meaning": "hibernation"
  },
  {
    "kanji": "蝿",
    "meaning": "housefly"
  },
  {
    "kanji": "蟻",
    "meaning": "ant"
  },
  {
    "kanji": "蜂",
    "meaning": "bee"
  },
  {
    "kanji": "蝋",
    "meaning": "wax"
  },
  {
    "kanji": "蝦",
    "meaning": "shrimp"
  },
  {
    "kanji": "蛸",
    "meaning": "octopus"
  },
  {
    "kanji": "螺",
    "meaning": "screw"
  },
  {
    "kanji": "蝉",
    "meaning": "cicada"
  },
  {
    "kanji": "蛙",
    "meaning": "frog"
  },
  {
    "kanji": "蛾",
    "meaning": "moth"
  },
  {
    "kanji": "蛤",
    "meaning": "clam"
  },
  {
    "kanji": "蛭",
    "meaning": "leech"
  },
  {
    "kanji": "蛎",
    "meaning": "oyster"
  },
  {
    "kanji": "罫",
    "meaning": "ruled lines"
  },
  {
    "kanji": "罵",
    "meaning": "insult"
  },
  {
    "kanji": "袈",
    "meaning": "stole"
  },
  {
    "kanji": "裟",
    "meaning": "monk's sash"
  },
  {
    "kanji": "戴",
    "meaning": "accept humbly"
  },
  {
    "kanji": "截",
    "meaning": "incision"
  },
  {
    "kanji": "哉",
    "meaning": "I wonder"
  },
  {
    "kanji": "詢",
    "meaning": "counsel"
  },
  {
    "kanji": "諄",
    "meaning": "polite"
  },
  {
    "kanji": "讐",
    "meaning": "vendetta"
  },
  {
    "kanji": "諌",
    "meaning": "remonstrate"
  },
  {
    "kanji": "謎",
    "meaning": "riddle"
  },
  {
    "kanji": "諒",
    "meaning": "verify"
  },
  {
    "kanji": "讃",
    "meaning": "compliment"
  },
  {
    "kanji": "誰",
    "meaning": "who?"
  },
  {
    "kanji": "訊",
    "meaning": "query"
  },
  {
    "kanji": "訣",
    "meaning": "split up"
  },
  {
    "kanji": "詣",
    "meaning": "visit a shrine"
  },
  {
    "kanji": "諦",
    "meaning": "give up"
  },
  {
    "kanji": "詮",
    "meaning": "elucidate"
  },
  {
    "kanji": "詑",
    "meaning": "prevarication"
  },
  {
    "kanji": "誼",
    "meaning": "familiarity"
  },
  {
    "kanji": "謬",
    "meaning": "fallible"
  },
  {
    "kanji": "詫",
    "meaning": "beg pardon"
  },
  {
    "kanji": "諏",
    "meaning": "advise"
  },
  {
    "kanji": "諺",
    "meaning": "proverb"
  },
  {
    "kanji": "誹",
    "meaning": "slander"
  },
  {
    "kanji": "謂",
    "meaning": "so-called"
  },
  {
    "kanji": "諜",
    "meaning": "secret agent"
  },
  {
    "kanji": "註",
    "meaning": "footnote"
  },
  {
    "kanji": "譬",
    "meaning": "parable"
  },
  {
    "kanji": "轟",
    "meaning": "rumble"
  },
  {
    "kanji": "輔",
    "meaning": "reinforce"
  },
  {
    "kanji": "輻",
    "meaning": "spoke"
  },
  {
    "kanji": "輯",
    "meaning": "assemble"
  },
  {
    "kanji": "貌",
    "meaning": "countenance"
  },
  {
    "kanji": "豹",
    "meaning": "panther"
  },
  {
    "kanji": "賎",
    "meaning": "despicable"
  },
  {
    "kanji": "貼",
    "meaning": "affix"
  },
  {
    "kanji": "貰",
    "meaning": "get"
  },
  {
    "kanji": "賂",
    "meaning": "graft"
  },
  {
    "kanji": "賑",
    "meaning": "bustling"
  },
  {
    "kanji": "躓",
    "meaning": "stumble"
  },
  {
    "kanji": "蹄",
    "meaning": "hoof"
  },
  {
    "kanji": "蹴",
    "meaning": "kick"
  },
  {
    "kanji": "蹟",
    "meaning": "vestiges"
  },
  {
    "kanji": "跨",
    "meaning": "straddle"
  },
  {
    "kanji": "跪",
    "meaning": "kneel"
  },
  {
    "kanji": "醤",
    "meaning": "soy sauce"
  },
  {
    "kanji": "醍",
    "meaning": "whey"
  },
  {
    "kanji": "酎",
    "meaning": "hooch"
  },
  {
    "kanji": "醐",
    "meaning": "ghee"
  },
  {
    "kanji": "醒",
    "meaning": "awakening"
  },
  {
    "kanji": "醇",
    "meaning": "strong saké"
  },
  {
    "kanji": "麺",
    "meaning": "noodles"
  },
  {
    "kanji": "麹",
    "meaning": "malt"
  },
  {
    "kanji": "釦",
    "meaning": "button"
  },
  {
    "kanji": "銚",
    "meaning": "keg"
  },
  {
    "kanji": "鋤",
    "meaning": "plow"
  },
  {
    "kanji": "鍋",
    "meaning": "pot"
  },
  {
    "kanji": "鏑",
    "meaning": "arrowhead"
  },
  {
    "kanji": "鋸",
    "meaning": "handsaw"
  },
  {
    "kanji": "錐",
    "meaning": "awl"
  },
  {
    "kanji": "鍵",
    "meaning": "key"
  },
  {
    "kanji": "鍬",
    "meaning": "hoe"
  },
  {
    "kanji": "鋲",
    "meaning": "rivet"
  },
  {
    "kanji": "錫",
    "meaning": "tin"
  },
  {
    "kanji": "錨",
    "meaning": "anchor"
  },
  {
    "kanji": "釘",
    "meaning": "nail"
  },
  {
    "kanji": "鑓",
    "meaning": "javelin"
  },
  {
    "kanji": "鋒",
    "meaning": "sword's point"
  },
  {
    "kanji": "鎚",
    "meaning": "hammer"
  },
  {
    "kanji": "鉦",
    "meaning": "carillion"
  },
  {
    "kanji": "錆",
    "meaning": "rust"
  },
  {
    "kanji": "鍾",
    "meaning": "cluster"
  },
  {
    "kanji": "鋏",
    "meaning": "scissors"
  },
  {
    "kanji": "閃",
    "meaning": "flash"
  },
  {
    "kanji": "悶",
    "meaning": "agony"
  },
  {
    "kanji": "閤",
    "meaning": "side gate"
  },
  {
    "kanji": "闇",
    "meaning": "pitch dark"
  },
  {
    "kanji": "雫",
    "meaning": "trickle"
  },
  {
    "kanji": "霞",
    "meaning": "haze"
  },
  {
    "kanji": "翰",
    "meaning": "quill"
  },
  {
    "kanji": "斡",
    "meaning": "auspices"
  },
  {
    "kanji": "鞍",
    "meaning": "saddle"
  },
  {
    "kanji": "鞭",
    "meaning": "whip"
  },
  {
    "kanji": "鞘",
    "meaning": "saddle straps"
  },
  {
    "kanji": "鞄",
    "meaning": "briefcase"
  },
  {
    "kanji": "靭",
    "meaning": "pliable"
  },
  {
    "kanji": "鞠",
    "meaning": "terminate"
  },
  {
    "kanji": "頓",
    "meaning": "immediate"
  },
  {
    "kanji": "顛",
    "meaning": "overturn"
  },
  {
    "kanji": "穎",
    "meaning": "brush tip"
  },
  {
    "kanji": "頃",
    "meaning": "about that time"
  },
  {
    "kanji": "頬",
    "meaning": "cheek"
  },
  {
    "kanji": "頗",
    "meaning": "exceedingly"
  },
  {
    "kanji": "頌",
    "meaning": "accolade"
  },
  {
    "kanji": "顎",
    "meaning": "chin"
  },
  {
    "kanji": "頚",
    "meaning": "neck and throat"
  },
  {
    "kanji": "餌",
    "meaning": "feed"
  },
  {
    "kanji": "餐",
    "meaning": "repast"
  },
  {
    "kanji": "饗",
    "meaning": "feast"
  },
  {
    "kanji": "蝕",
    "meaning": "eclipse"
  },
  {
    "kanji": "飴",
    "meaning": "sweets"
  },
  {
    "kanji": "餅",
    "meaning": "mochi"
  },
  {
    "kanji": "駕",
    "meaning": "stretcher"
  },
  {
    "kanji": "騨",
    "meaning": "piebald"
  },
  {
    "kanji": "馳",
    "meaning": "rush"
  },
  {
    "kanji": "騙",
    "meaning": "cheat"
  },
  {
    "kanji": "馴",
    "meaning": "tame"
  },
  {
    "kanji": "駁",
    "meaning": "rebuttal"
  },
  {
    "kanji": "駈",
    "meaning": "gallop"
  },
  {
    "kanji": "驢",
    "meaning": "donkey"
  },
  {
    "kanji": "鰻",
    "meaning": "eel"
  },
  {
    "kanji": "鯛",
    "meaning": "sea bream"
  },
  {
    "kanji": "鰯",
    "meaning": "sardine"
  },
  {
    "kanji": "鱒",
    "meaning": "trout"
  },
  {
    "kanji": "鮭",
    "meaning": "salmon"
  },
  {
    "kanji": "鮪",
    "meaning": "tuna"
  },
  {
    "kanji": "鮎",
    "meaning": "sweet smelt"
  },
  {
    "kanji": "鯵",
    "meaning": "horse mackerel"
  },
  {
    "kanji": "鱈",
    "meaning": "cod"
  },
  {
    "kanji": "鯖",
    "meaning": "mackerel"
  },
  {
    "kanji": "鮫",
    "meaning": "shark"
  },
  {
    "kanji": "鰹",
    "meaning": "bonito"
  },
  {
    "kanji": "鰍",
    "meaning": "bullhead"
  },
  {
    "kanji": "鰐",
    "meaning": "alligator"
  },
  {
    "kanji": "鮒",
    "meaning": "crucian"
  },
  {
    "kanji": "鮨",
    "meaning": "sushi"
  },
  {
    "kanji": "鰭",
    "meaning": "fish fin"
  },
  {
    "kanji": "鴎",
    "meaning": "seagull"
  },
  {
    "kanji": "鵬",
    "meaning": "roc"
  },
  {
    "kanji": "鸚",
    "meaning": "parakeet"
  },
  {
    "kanji": "鵡",
    "meaning": "parrot"
  },
  {
    "kanji": "鵜",
    "meaning": "cormorant"
  },
  {
    "kanji": "鷺",
    "meaning": "heron"
  },
  {
    "kanji": "鷲",
    "meaning": "eagle"
  },
  {
    "kanji": "鴨",
    "meaning": "wild duck"
  },
  {
    "kanji": "鳶",
    "meaning": "kite falcon"
  },
  {
    "kanji": "梟",
    "meaning": "owl"
  },
  {
    "kanji": "塵",
    "meaning": "dust"
  },
  {
    "kanji": "麓",
    "meaning": "foot of a mountain"
  },
  {
    "kanji": "麒",
    "meaning": "giraffe"
  },
  {
    "kanji": "冥",
    "meaning": "Hades"
  },
  {
    "kanji": "瞑",
    "meaning": "close the eyes"
  },
  {
    "kanji": "暝",
    "meaning": "murky"
  },
  {
    "kanji": "坐",
    "meaning": "sitting in mediation"
  },
  {
    "kanji": "挫",
    "meaning": "sprain"
  },
  {
    "kanji": "朔",
    "meaning": "first day of the month"
  },
  {
    "kanji": "遡",
    "meaning": "go upstream"
  },
  {
    "kanji": "曳",
    "meaning": "drag"
  },
  {
    "kanji": "洩",
    "meaning": "dribble out"
  },
  {
    "kanji": "彗",
    "meaning": "comet"
  },
  {
    "kanji": "慧",
    "meaning": "astute"
  },
  {
    "kanji": "嘉",
    "meaning": "applaud"
  },
  {
    "kanji": "兇",
    "meaning": "evil"
  },
  {
    "kanji": "兜",
    "meaning": "helmet"
  },
  {
    "kanji": "爽",
    "meaning": "bracing"
  },
  {
    "kanji": "欝",
    "meaning": "depressed"
  },
  {
    "kanji": "劫",
    "meaning": "kalpa"
  },
  {
    "kanji": "勃",
    "meaning": "erection"
  },
  {
    "kanji": "歎",
    "meaning": "bemoan"
  },
  {
    "kanji": "輿",
    "meaning": "palanquin"
  },
  {
    "kanji": "巽",
    "meaning": "southeast"
  },
  {
    "kanji": "歪",
    "meaning": "warped"
  },
  {
    "kanji": "翠",
    "meaning": "jade green"
  },
  {
    "kanji": "黛",
    "meaning": "blue-black"
  },
  {
    "kanji": "鼎",
    "meaning": "tripod"
  },
  {
    "kanji": "鹵",
    "meaning": "rocksalt"
  },
  {
    "kanji": "鹸",
    "meaning": "lye"
  },
  {
    "kanji": "虔",
    "meaning": "reserved"
  },
  {
    "kanji": "燕",
    "meaning": "swallow"
  },
  {
    "kanji": "嘗",
    "meaning": "lick"
  },
  {
    "kanji": "殆",
    "meaning": "almost"
  },
  {
    "kanji": "孟",
    "meaning": "start"
  },
  {
    "kanji": "牌",
    "meaning": "mahjong tiles"
  },
  {
    "kanji": "骸",
    "meaning": "remains"
  },
  {
    "kanji": "覗",
    "meaning": "peek"
  },
  {
    "kanji": "彪",
    "meaning": "mottled"
  },
  {
    "kanji": "秦",
    "meaning": "Manchu dynasty"
  },
  {
    "kanji": "雀",
    "meaning": "sparrow"
  },
  {
    "kanji": "隼",
    "meaning": "peregrine falcon"
  },
  {
    "kanji": "耀",
    "meaning": "shimmering"
  },
  {
    "kanji": "夷",
    "meaning": "ebisu"
  },
  {
    "kanji": "戚",
    "meaning": "relatives"
  },
  {
    "kanji": "嚢",
    "meaning": "cyst"
  },
  {
    "kanji": "丼",
    "meaning": "domburi"
  },
  {
    "kanji": "暢",
    "meaning": "carefree"
  },
  {
    "kanji": "廻",
    "meaning": "circling"
  },
  {
    "kanji": "畿",
    "meaning": "capital suburbs"
  },
  {
    "kanji": "欣",
    "meaning": "elation"
  },
  {
    "kanji": "毅",
    "meaning": "stalwart"
  },
  {
    "kanji": "斯",
    "meaning": "this"
  },
  {
    "kanji": "匙",
    "meaning": "wooden spoon"
  },
  {
    "kanji": "匡",
    "meaning": "set straight"
  },
  {
    "kanji": "肇",
    "meaning": "founding"
  },
  {
    "kanji": "麿",
    "meaning": "Utamaro"
  },
  {
    "kanji": "叢",
    "meaning": "conglomerate"
  },
  {
    "kanji": "肴",
    "meaning": "entreat"
  },
  {
    "kanji": "斐",
    "meaning": "symmetrically patterned"
  },
  {
    "kanji": "卿",
    "meaning": "magistrate"
  },
  {
    "kanji": "翫",
    "meaning": "fiddle with"
  },
  {
    "kanji": "於",
    "meaning": "within"
  },
  {
    "kanji": "套",
    "meaning": "hackneyed"
  },
  {
    "kanji": "叛",
    "meaning": "rebellion"
  },
  {
    "kanji": "尖",
    "meaning": "sharp point"
  },
  {
    "kanji": "壷",
    "meaning": "crock"
  },
  {
    "kanji": "叡",
    "meaning": "sapience"
  },
  {
    "kanji": "酋",
    "meaning": "chieftain"
  },
  {
    "kanji": "鴬",
    "meaning": "nightingale"
  },
  {
    "kanji": "赫",
    "meaning": "incandescent"
  },
  {
    "kanji": "臥",
    "meaning": "supinate"
  },
  {
    "kanji": "甥",
    "meaning": "nephew"
  },
  {
    "kanji": "瓢",
    "meaning": "gourd"
  },
  {
    "kanji": "琵",
    "meaning": "biwa"
  },
  {
    "kanji": "琶",
    "meaning": "lute"
  },
  {
    "kanji": "叉",
    "meaning": "forked"
  },
  {
    "kanji": "舜",
    "meaning": "rose of Sharon"
  },
  {
    "kanji": "畠",
    "meaning": "dry field"
  },
  {
    "kanji": "拳",
    "meaning": "fist"
  },
  {
    "kanji": "圃",
    "meaning": "vegetable patch"
  },
  {
    "kanji": "丞",
    "meaning": "helping hand"
  },
  {
    "kanji": "亮",
    "meaning": "translucent"
  },
  {
    "kanji": "胤",
    "meaning": "blood relative"
  },
  {
    "kanji": "疏",
    "meaning": "transcription"
  },
  {
    "kanji": "膏",
    "meaning": "ointment"
  },
  {
    "kanji": "魁",
    "meaning": "pioneer"
  },
  {
    "kanji": "馨",
    "meaning": "ambrosial"
  },
  {
    "kanji": "牒",
    "meaning": "label"
  },
  {
    "kanji": "瞥",
    "meaning": "glimpse"
  },
  {
    "kanji": "阜",
    "meaning": "large hill"
  },
  {
    "kanji": "睾",
    "meaning": "testicle"
  },
  {
    "kanji": "巫",
    "meaning": "sorceress"
  },
  {
    "kanji": "敦",
    "meaning": "empathetic"
  },
  {
    "kanji": "奎",
    "meaning": "Andromeda"
  },
  {
    "kanji": "翔",
    "meaning": "soar"
  },
  {
    "kanji": "皓",
    "meaning": "beaming"
  },
  {
    "kanji": "黎",
    "meaning": "tenebrous"
  },
  {
    "kanji": "赳",
    "meaning": "bold"
  },
  {
    "kanji": "已",
    "meaning": "stop short"
  },
  {
    "kanji": "棘",
    "meaning": "thornbush"
  },
  {
    "kanji": "聚",
    "meaning": "crowd"
  },
  {
    "kanji": "甦",
    "meaning": "resucitate"
  },
  {
    "kanji": "剪",
    "meaning": "pruning"
  },
  {
    "kanji": "躾",
    "meaning": "upbringing"
  },
  {
    "kanji": "夥",
    "meaning": "plentiful"
  },
  {
    "kanji": "鼾",
    "meaning": "snore"
  },
  {
    "kanji": "祟",
    "meaning": "cast a spell"
  },
  {
    "kanji": "粁",
    "meaning": "kilometer"
  },
  {
    "kanji": "糎",
    "meaning": "centimeter"
  },
  {
    "kanji": "粍",
    "meaning": "millimeter"
  },
  {
    "kanji": "噸",
    "meaning": "ton"
  },
  {
    "kanji": "哩",
    "meaning": "mile"
  },
  {
    "kanji": "浬",
    "meaning": "nautical mile"
  },
  {
    "kanji": "吋",
    "meaning": "inch"
  },
  {
    "kanji": "呎",
    "meaning": "feet"
  },
  {
    "kanji": "梵",
    "meaning": "brahman"
  },
  {
    "kanji": "陀",
    "meaning": "Shakyamuni Buddha"
  },
  {
    "kanji": "薩",
    "meaning": "bodhisattva"
  },
  {
    "kanji": "菩",
    "meaning": "bo tree"
  },
  {
    "kanji": "唖",
    "meaning": "babble"
  },
  {
    "kanji": "迦",
    "meaning": "Sanskrit ka"
  },
  {
    "kanji": "那",
    "meaning": "interrogative"
  },
  {
    "kanji": "牟",
    "meaning": "moo"
  },
  {
    "kanji": "珈",
    "meaning": "jeweled hairpin"
  },
  {
    "kanji": "琲",
    "meaning": "beaded hairpin"
  },
  {
    "kanji": "檜",
    "meaning": "Japanese cypress [old]"
  },
  {
    "kanji": "轡",
    "meaning": "bridle's bit"
  },
  {
    "kanji": "淵",
    "meaning": "abyss [old]"
  },
  {
    "kanji": "伍",
    "meaning": "V"
  },
  {
    "kanji": "什",
    "meaning": "X"
  },
  {
    "kanji": "萬",
    "meaning": "ten thousand [old]"
  },
  {
    "kanji": "邁",
    "meaning": "pass through"
  },
  {
    "kanji": "逞",
    "meaning": "tough"
  },
  {
    "kanji": "燈",
    "meaning": "lamp [old]"
  },
  {
    "kanji": "裡",
    "meaning": "back [old]"
  },
  {
    "kanji": "薗",
    "meaning": "park [alternate]"
  },
  {
    "kanji": "鋪",
    "meaning": "shop [alternate]"
  },
  {
    "kanji": "嶋",
    "meaning": "island [alternate]"
  },
  {
    "kanji": "峯",
    "meaning": "summit [alternate]"
  },
  {
    "kanji": "巌",
    "meaning": "boulder [old]"
  },
  {
    "kanji": "埜",
    "meaning": "plains [old]"
  },
  {
    "kanji": "舘",
    "meaning": "Bldg. [old]"
  },
  {
    "kanji": "龍",
    "meaning": "dragon [old]"
  },
  {
    "kanji": "寵",
    "meaning": "patronage"
  },
  {
    "kanji": "聾",
    "meaning": "deafness"
  },
  {
    "kanji": "慾",
    "meaning": "longing [old]"
  },
  {
    "kanji": "亙",
    "meaning": "span [old]"
  },
  {
    "kanji": "躯",
    "meaning": "body [old]"
  },
  {
    "kanji": "嶽",
    "meaning": "Point [old]"
  },
  {
    "kanji": "國",
    "meaning": "country [old]"
  },
  {
    "kanji": "脛",
    "meaning": "shin"
  },
  {
    "kanji": "勁",
    "meaning": "formidable"
  },
  {
    "kanji": "箋",
    "meaning": "stationary"
  },
  {
    "kanji": "祀",
    "meaning": "enshrine"
  },
  {
    "kanji": "祓",
    "meaning": "exorcism"
  },
  {
    "kanji": "躇",
    "meaning": "dither"
  },
  {
    "kanji": "壽",
    "meaning": "longevity [old]"
  },
  {
    "kanji": "躊",
    "meaning": "hesitate"
  },
  {
    "kanji": "彙",
    "meaning": "glossary"
  },
  {
    "kanji": "饅",
    "meaning": "bean jam"
  },
  {
    "kanji": "嘔",
    "meaning": "retch"
  },
  {
    "kanji": "鼈",
    "meaning": "snapping turtle"
  },
  {
    "kanji": "亨",
    "meaning": "go smoothly"
  },
  {
    "kanji": "侑",
    "meaning": "condone"
  },
  {
    "kanji": "梧",
    "meaning": "parasol tree"
  },
  {
    "kanji": "欽",
    "meaning": "circumspect"
  },
  {
    "kanji": "煕",
    "meaning": "cheer"
  },
  {
    "kanji": "而",
    "meaning": "and then"
  },
  {
    "kanji": "掟",
    "meaning": "mandate"
  },
  {
    "kanji": "嗅",
    "meaning": "sniff"
  },
  {
    "kanji": "喩",
    "meaning": "metaphor"
  },
  {
    "kanji": "訃",
    "meaning": "obituary"
  },
  {
    "kanji": "楷",
    "meaning": "block letters"
  },
  {
    "kanji": "諧",
    "meaning": "orderliness"
  },
  {
    "kanji": "錮",
    "meaning": "weld"
  },
  {
    "kanji": "恣",
    "meaning": "selfish"
  },
  {
    "kanji": "惧",
    "meaning": "disquieting"
  },
  {
    "kanji": "憬",
    "meaning": "hanker"
  },
  {
    "kanji": "拉",
    "meaning": "yank"
  },
  {
    "kanji": "傲",
    "meaning": "arrogance"
  },
  {
    "kanji": "踪",
    "meaning": "trail"
  },
  {
    "kanji": "緻",
    "meaning": "fine"
  },
  {
    "kanji": "璧",
    "meaning": "holed gem"
  },
  {
    "kanji": "摯",
    "meaning": "clasp"
  },
  {
    "kanji": "貪",
    "meaning": "covet"
  },
  {
    "kanji": "慄",
    "meaning": "shudder"
  },
  {
    "kanji": "辣",
    "meaning": "bitter"
  },
  {
    "kanji": "瘍",
    "meaning": "carbuncle"
  },
  {
    "kanji": "哺",
    "meaning": "suckle"
  },
  {
    "kanji": "籠",
    "meaning": "cage [old]"
  },
  {
    "kanji": "羞",
    "meaning": "humiliate"
  },
  {
    "kanji": "鬱",
    "meaning": "gloom"
  }
 ];
const search = ref('');
const random = ref(undefined);
const show = ref(false);
function getRandomKanji() {
  random.value = kanjis[Math.floor(Math.random() * kanjis.length)];
  show.value = false;
};


</script>
