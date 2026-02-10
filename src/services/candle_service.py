import json
import os
from typing import List, Dict, Optional, Union
from src.core.paths import DATA_FILE


class CandleService:
    def __init__(self):
        """
        تهيئة السيرفيس مع مسار ملف JSON

        Args:
            json_file_path (str): مسار ملف JSON
        """
        self.json_file_path = DATA_FILE
        self.candles = self._load_candles()

    def _load_candles(self) -> List[Dict]:
        """
        تحميل بيانات الشموع من ملف JSON

        Returns:
            List[Dict]: قائمة تحتوي على جميع الشموع
        """
        try:
            if not os.path.exists(self.json_file_path):
                raise FileNotFoundError(f"الملف {self.json_file_path} غير موجود")

            with open(self.json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            return data

        except json.JSONDecodeError as e:
            print(f"خطأ في قراءة ملف JSON: {e}")
            return []
        except Exception as e:
            print(f"خطأ غير متوقع: {e}")
            return []

    def get_all_candles(self) -> List[Dict]:
        """
        الحصول على جميع الشموع اليابانية

        Returns:
            List[Dict]: قائمة بجميع الشموع
        """
        return self.candles

    def get_reversal_candles(self) -> List[Dict]:
        """
        الحصول على شموع الانعكاس فقط

        Returns:
            List[Dict]: قائمة بشموع الانعكاس
        """
        return [candle for candle in self.candles if candle.get("candle_type") == "Reversal"]

    def get_continuation_candles(self) -> List[Dict]:
        """
        الحصول على شموع الاستمرارية فقط

        Returns:
            List[Dict]: قائمة بشموع الاستمرارية
        """
        return [candle for candle in self.candles if candle.get("candle_type") == "Continuation"]

    def get_indecision_candles(self) -> List[Dict]:
        """
        الحصول على شموع التردد فقط

        Returns:
            List[Dict]: قائمة بشموع التردد
        """
        return [candle for candle in self.candles if candle.get("candle_type") == "Indecision"]

    def get_bullish_candles(self) -> List[Dict]:
        """
        الحصول على الشموع الصعودية

        Returns:
            List[Dict]: قائمة بالشموع الصعودية
        """
        return [candle for candle in self.candles if candle.get("trend") == "Bullish"]

    def get_bearish_candles(self) -> List[Dict]:
        """
        الحصول على الشموع الهابطة

        Returns:
            List[Dict]: قائمة بالشموع الهابطة
        """
        return [candle for candle in self.candles if candle.get("trend") == "Bearish"]

    def get_neutral_candles(self) -> List[Dict]:
        """
        الحصول على الشموع المحايدة

        Returns:
            List[Dict]: قائمة بالشموع المحايدة
        """
        return [candle for candle in self.candles if candle.get("trend") == "Neutral"]

    def get_bullish_reversal_candles(self) -> List[Dict]:
        """
        الحصول على شموع الانعكاس الصعودية فقط

        Returns:
            List[Dict]: قائمة بشموع الانعكاس الصعودية
        """
        return [candle for candle in self.candles
                if candle.get("candle_type") == "Reversal"
                and candle.get("trend") == "Bullish"]

    def get_bearish_reversal_candles(self) -> List[Dict]:
        """
        الحصول على شموع الانعكاس الهابطة فقط

        Returns:
            List[Dict]: قائمة بشموع الانعكاس الهابطة
        """
        return [candle for candle in self.candles
                if candle.get("candle_type") == "Reversal"
                and candle.get("trend") == "Bearish"]

    def get_candle_by_id(self, candle_id: int) -> Optional[Dict]:
        """
        البحث عن شمعة باستخدام المعرف

        Args:
            candle_id (int): معرف الشمعة

        Returns:
            Optional[Dict]: بيانات الشمعة أو None إذا لم توجد
        """
        for candle in self.candles:
            if candle.get("id") == candle_id:
                return candle
        return None

    def get_candle_by_name(self, name: str, language: str = "ar") -> List[Dict]:
        """
        البحث عن شمعة باستخدام الاسم

        Args:
            name (str): اسم الشمعة للبحث عنه
            language (str): لغة البحث ('ar' للعربية أو 'en' للإنجليزية)

        Returns:
            List[Dict]: قائمة بالشموع التي تطابق البحث
        """
        results = []
        name_lower = name.lower()

        for candle in self.candles:
            if language == "ar":
                candle_name = candle.get("name_ar", "").lower()
            else:
                candle_name = candle.get("name_en", "").lower()

            if name_lower in candle_name:
                results.append(candle)

        return results

    def get_candles_by_type(self, candle_type: str) -> List[Dict]:
        """
        الحصول على الشموع حسب النوع

        Args:
            candle_type (str): نوع الشموع ('Reversal', 'Continuation', 'Indecision')

        Returns:
            List[Dict]: قائمة بالشموع من النوع المحدد
        """
        valid_types = ["Reversal", "Continuation", "Indecision"]
        if candle_type not in valid_types:
            print(f"تحذير: النوع {candle_type} غير صالح. الأنواع الصالحة: {valid_types}")
            return []

        return [candle for candle in self.candles if candle.get("candle_type") == candle_type]

    def get_candles_by_trend(self, trend: str) -> List[Dict]:
        """
        الحصول على الشموع حسب الاتجاه

        Args:
            trend (str): اتجاه الشموع ('Bullish', 'Bearish', 'Neutral')

        Returns:
            List[Dict]: قائمة بالشموع من الاتجاه المحدد
        """
        valid_trends = ["Bullish", "Bearish", "Neutral"]
        if trend not in valid_trends:
            print(f"تحذير: الاتجاه {trend} غير صالح. الاتجاهات الصالحة: {valid_trends}")
            return []

        return [candle for candle in self.candles if candle.get("trend") == trend]

    def get_candle_count_by_type(self) -> Dict[str, int]:
        """
        الحصول على عدد الشموع حسب النوع

        Returns:
            Dict[str, int]: قاموس بعدد الشموع لكل نوع
        """
        counts = {
            "Reversal": len(self.get_reversal_candles()),
            "Continuation": len(self.get_continuation_candles()),
            "Indecision": len(self.get_indecision_candles())
        }
        return counts

    def get_candle_count_by_trend(self) -> Dict[str, int]:
        """
        الحصول على عدد الشموع حسب الاتجاه

        Returns:
            Dict[str, int]: قاموس بعدد الشموع لكل اتجاه
        """
        counts = {
            "Bullish": len(self.get_bullish_candles()),
            "Bearish": len(self.get_bearish_candles()),
            "Neutral": len(self.get_neutral_candles())
        }
        return counts

    def search_candles(self, keyword: str) -> List[Dict]:
        """
        بحث عام في جميع حقول الشموع

        Args:
            keyword (str): الكلمة المفتاحية للبحث

        Returns:
            List[Dict]: قائمة بالشموع التي تطابق البحث
        """
        results = []
        keyword_lower = keyword.lower()

        for candle in self.candles:
            # البحث في جميع الحقول النصية
            fields_to_search = ["name_ar", "name_en", "description", "rules"]

            for field in fields_to_search:
                field_value = candle.get(field, "")
                if keyword_lower in str(field_value).lower():
                    results.append(candle)
                    break  # لا نحتاج للبحث في باقي الحقول لنفس الشمعة

        return results

    def print_candle_info(self, candle: Dict):
        """
        طباعة معلومات شمعة بشكل منظم

        Args:
            candle (Dict): بيانات الشمعة
        """
        if not candle:
            print("الشمعة غير موجودة")
            return

        print("=" * 50)
        print(f"المعرف: {candle.get('id')}")
        print(f"الاسم العربي: {candle.get('name_ar')}")
        print(f"الاسم الإنجليزي: {candle.get('name_en')}")
        print(f"النوع: {candle.get('candle_type')}")
        print(f"الاتجاه: {candle.get('trend')}")
        print(f"الوصف: {candle.get('description')}")
        print(f"شروط التحقق: {candle.get('rules')}")
        print("=" * 50)

    def save_to_file(self, candles: List[Dict], file_path: str):
        """
        حفظ قائمة شموع إلى ملف JSON

        Args:
            candles (List[Dict]): قائمة الشموع للحفظ
            file_path (str): مسار الملف للحفظ
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(candles, file, ensure_ascii=False, indent=2)
            print(f"تم حفظ {len(candles)} شمعة في {file_path}")
        except Exception as e:
            print(f"خطأ في حفظ الملف: {e}")


# مثال على الاستخدام
if __name__ == "__main__":
    # إنشاء كائن من السيرفيس
    service = CandleService("japanese_candles.json")

    # اختبار الدوال الأساسية
    print("عدد جميع الشموع:", len(service.get_all_candles()))
    print("عدد شموع الانعكاس:", len(service.get_reversal_candles()))
    print("عدد الشموع الصعودية:", len(service.get_bullish_candles()))
    print("عدد شموع الانعكاس الصعودية:", len(service.get_bullish_reversal_candles()))

    # الحصول على تعداد حسب النوع
    print("\nتعداد الشموع حسب النوع:")
    type_counts = service.get_candle_count_by_type()
    for candle_type, count in type_counts.items():
        print(f"  {candle_type}: {count}")

    # البحث عن شمعة محددة
    print("\nالبحث عن شمعة 'المطرقة':")
    hammer_candles = service.get_candle_by_name("المطرقة", "ar")
    if hammer_candles:
        service.print_candle_info(hammer_candles[0])

    # البحث بالمعرف
    print("\nالبحث عن الشمعة ذات المعرف 1:")
    candle = service.get_candle_by_id(1)
    if candle:
        service.print_candle_info(candle)

    # بحث عام
    print("\nالبحث عن كلمة 'صعودي':")
    search_results = service.search_candles("صعودي")
    print(f"عدد النتائج: {len(search_results)}")

    # الحصول على شموع التردد
    print("\nشموع التردد:")
    indecision_candles = service.get_indecision_candles()
    for candle in indecision_candles:
        print(f"  - {candle.get('name_ar')} ({candle.get('name_en')})")
