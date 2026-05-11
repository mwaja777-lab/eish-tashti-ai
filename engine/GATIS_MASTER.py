# EISH TASHTI AI - Master Orchestrator V2.0
# Global Executive Standard | 7:3 Strategy

import json
import os
from engine.logic import TradingLogic
from ui.display import BrandDisplay

def load_credentials():
    # تحميل مفاتيح العبور من الملف رقم 1
    with open('config/credentials.json', 'r') as f:
        return json.load(f)

def start_engine():
    # استدعاء الهوية البصرية والمنطق البرمجي
    display = BrandDisplay()
    logic = TradingLogic()
    
    # 💎 نحت الشعار الماسي في الواجهة
    display.show_gold_logo()
    display.show_secure_boot()
    
    # ربط البيانات
    try:
        creds = load_credentials()
        print(f"\n[SYSTEM]: CONNECTED TO {creds['account_type']} ACCOUNT")
        print(f"[LOGIC]: RATIO {logic.risk_reward_ratio} ACTIVATED")
        
        # جس نبض السوق الأول (تجريبي)
        display.update_dashboard(price="2345.60 (GOLD)", status="SCANNING", target="2365.00")
        
        print("\n>>> EISH TASHTI AI IS LIVE AND READY.")
    except Exception as e:
        print(f"\n[ERROR]: FAILED TO LOAD SYSTEM: {e}")

if __name__ == "__main__":
    start_engine()
  
