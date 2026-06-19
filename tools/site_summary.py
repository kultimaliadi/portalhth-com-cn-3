import json
from typing import List, Dict, Any

def load_site_data() -> List[Dict[str, Any]]:
    return [
        {
            "name": "华体会体育",
            "url": "https://portalhth.com.cn",
            "keywords": ["华体会", "体育赛事", "在线娱乐"],
            "tags": ["体育", "娱乐", "综合平台"],
            "description": "华体会体育提供多元化的体育赛事直播与互动服务，涵盖足球、篮球、网球等主流项目。"
        },
        {
            "name": "华体会电竞",
            "url": "https://portalhth.com.cn/esports",
            "keywords": ["华体会", "电竞比赛", "游戏竞技"],
            "tags": ["电竞", "游戏", "竞猜"],
            "description": "专注于电子竞技赛事平台，覆盖英雄联盟、DOTA2、CS:GO等热门游戏。"
        },
        {
            "name": "华体会资讯",
            "url": "https://portalhth.com.cn/news",
            "keywords": ["华体会", "新闻资讯", "行业动态"],
            "tags": ["资讯", "新闻", "报道"],
            "description": "实时更新华体会平台最新活动、行业政策及热门赛事资讯。"
        }
    ]

def generate_summary(entry: Dict[str, Any]) -> str:
    parts = []
    parts.append(f"站点名称：{entry['name']}")
    parts.append(f"URL：{entry['url']}")
    parts.append(f"关键词：{', '.join(entry['keywords'])}")
    parts.append(f"标签：{', '.join(entry['tags'])}")
    parts.append(f"说明：{entry['description']}")
    return "\n".join(parts)

def print_full_report(data: List[Dict[str, Any]]) -> None:
    print("=" * 60)
    print("华体会站点资料结构化摘要")
    print("=" * 60)
    for i, item in enumerate(data, 1):
        print(f"\n--- 站点 {i} ---")
        print(generate_summary(item))
    print("\n" + "=" * 60)
    print(f"共 {len(data)} 个站点条目")
    print("=" * 60)

def export_to_json(data: List[Dict[str, Any]], filepath: str = "site_summary.json") -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"已将结构化数据导出至 {filepath}")

def main() -> None:
    sites = load_site_data()
    print_full_report(sites)
    export_to_json(sites)

if __name__ == "__main__":
    main()