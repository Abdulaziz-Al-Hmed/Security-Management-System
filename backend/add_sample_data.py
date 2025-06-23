import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from sqlalchemy.orm import Session
from app.database.database import SessionLocal, create_tables
from app.models.employee import Employee
from app.models.contractor import Contractor
from app.models.vehicle import Vehicle
from datetime import date

def add_sample_data():
    print("🔄 جاري إضافة البيانات التجريبية...")
    create_tables()
    db = SessionLocal()
    
    try:
        # Add sample employees
        print("📋 إضافة الموظفين...")
        if db.query(Employee).count() == 0:
            employees = [
                Employee(
                    employee_id="EMP001",
                    full_name="Ahmed Mohammed Ali",
                    full_name_ar="أحمد محمد علي",
                    department="الأمان والحماية",
                    position="ضابط أمن",
                    phone="0555123456",
                    hire_date=date(2023, 1, 15),
                    is_active=True
                ),
                Employee(
                    employee_id="EMP002",
                    full_name="Fatima Ali Hassan",
                    full_name_ar="فاطمة علي حسن",
                    department="الإدارة",
                    position="مديرة إدارية",
                    phone="0555789012",
                    hire_date=date(2023, 3, 10),
                    is_active=True
                ),
                Employee(
                    employee_id="EMP003",
                    full_name="Mohammed Salem Omar",
                    full_name_ar="محمد سالم عمر",
                    department="التقنية",
                    position="فني تقني",
                    phone="0555345678",
                    hire_date=date(2023, 2, 20),
                    is_active=True
                ),
                Employee(
                    employee_id="EMP004",
                    full_name="Sara Ahmed Khalid",
                    full_name_ar="سارة أحمد خالد",
                    department="الموارد البشرية",
                    position="أخصائية موارد بشرية",
                    phone="0555456789",
                    hire_date=date(2023, 4, 5),
                    is_active=True
                ),
                Employee(
                    employee_id="EMP005",
                    full_name="Abdullah Fahad Ali",
                    full_name_ar="عبدالله فهد علي",
                    department="الأمان والحماية",
                    position="رئيس قسم الأمان",
                    phone="0555567890",
                    hire_date=date(2022, 6, 1),
                    is_active=True
                )
            ]
            
            for emp in employees:
                db.add(emp)
            
            print(f"✅ تم إضافة {len(employees)} موظف")
        else:
            print("ℹ️ الموظفون موجودون بالفعل")
        
        # Add sample contractors
        print("🏢 إضافة المقاولين...")
        if db.query(Contractor).count() == 0:
            contractors = [
                Contractor(
                    contractor_id="CON001",
                    full_name="Omar Hassan Ibrahim",
                    full_name_ar="عمر حسن إبراهيم",
                    company_name="Tech Solutions Company",
                    company_name_ar="شركة الحلول التقنية",
                    project_name="نظام صيانة الشبكات",
                    phone="0555999888",
                    contract_start_date=date(2023, 1, 1),
                    contract_end_date=date(2023, 12, 31),
                    is_active=True
                ),
                Contractor(
                    contractor_id="CON002",
                    full_name="Layla Ahmed Mohammed",
                    full_name_ar="ليلى أحمد محمد",
                    company_name="Al-Nour Cleaning Services",
                    company_name_ar="شركة النور لخدمات التنظيف",
                    project_name="تنظيف وصيانة المرافق",
                    phone="0555777666",
                    contract_start_date=date(2023, 1, 1),
                    contract_end_date=date(2023, 12, 31),
                    is_active=True
                ),
                Contractor(
                    contractor_id="CON003",
                    full_name="Khalid Salman Nasser",
                    full_name_ar="خالد سلمان ناصر",
                    company_name="Security Guard Services",
                    company_name_ar="شركة خدمات الحراسة الأمنية",
                    project_name="خدمات الحراسة الليلية",
                    phone="0555888777",
                    contract_start_date=date(2023, 3, 1),
                    contract_end_date=date(2024, 2, 29),
                    is_active=True
                ),
                Contractor(
                    contractor_id="CON004",
                    full_name="Amina Fahd Abdullah",
                    full_name_ar="أمينة فهد عبدالله",
                    company_name="Catering Excellence",
                    company_name_ar="شركة التميز للتموين",
                    project_name="خدمات التموين والضيافة",
                    phone="0555111222",
                    contract_start_date=date(2023, 2, 15),
                    contract_end_date=date(2023, 11, 15),
                    is_active=True
                )
            ]
            
            for contractor in contractors:
                db.add(contractor)
            
            print(f"✅ تم إضافة {len(contractors)} مقاول")
        else:
            print("ℹ️ المقاولون موجودون بالفعل")
        
        # Add sample vehicles - بأسماء الحقول الصحيحة
        print("🚗 إضافة المركبات...")
        if db.query(Vehicle).count() == 0:
            vehicles = [
                Vehicle(
                    plate_number="أ ب ج 1234",
                    vehicle_type="سيارة",
                    brand="تويوتا",  # استخدام brand بدلاً من make
                    model="كامري",
                    year=2022,
                    color="أبيض",
                    color_ar="أبيض",
                    owner_type="employee",
                    owner_id=1,  # سيتم ربطه بالموظف الأول
                    is_active=True,
                    is_authorized=True
                ),
                Vehicle(
                    plate_number="هـ و ز 5678",
                    vehicle_type="حافلة",
                    brand="مرسيدس",
                    model="سبرينتر",
                    year=2021,
                    color="أزرق",
                    color_ar="أزرق",
                    owner_type="contractor",
                    owner_id=1,  # سيتم ربطه بالمقاول الأول
                    is_active=True,
                    is_authorized=True
                ),
                Vehicle(
                    plate_number="د ذ ر 9999",
                    vehicle_type="شاحنة",
                    brand="فولفو",
                    model="FH16",
                    year=2020,
                    color="أحمر",
                    color_ar="أحمر",
                    owner_type="contractor",
                    owner_id=2,
                    is_active=True,
                    is_authorized=True
                ),
                Vehicle(
                    plate_number="س ش ص 7777",
                    vehicle_type="سيارة",
                    brand="نيسان",
                    model="التيما",
                    year=2023,
                    color="أسود",
                    color_ar="أسود",
                    owner_type="employee",
                    owner_id=2,
                    is_active=True,
                    is_authorized=True
                )
            ]
            
            for vehicle in vehicles:
                db.add(vehicle)
            
            print(f"✅ تم إضافة {len(vehicles)} مركبة")
        else:
            print("ℹ️ المركبات موجودة بالفعل")
        
        db.commit()
        print("\n🎉 تم إضافة جميع البيانات التجريبية بنجاح!")
        
        # Print summary
        employees_count = db.query(Employee).count()
        contractors_count = db.query(Contractor).count()
        vehicles_count = db.query(Vehicle).count()
        
        print(f"\n📊 ملخص البيانات:")
        print(f"   👥 الموظفون: {employees_count}")
        print(f"   🏢 المقاولون: {contractors_count}")
        print(f"   🚗 المركبات: {vehicles_count}")
        
    except Exception as e:
        print(f"❌ خطأ في إضافة البيانات: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_sample_data()