#include <iostream>
#include <pqxx/pqxx>

using namespace std;
using namespace pqxx;


class PortfolioRecord {
    string actif;
    float pu;
    string recordDate;
    public:
        void setActif(string s) { actif = s; }
        string getActif() { return actif; }
        void setPu(const pqxx::row::reference unitprice) { pu = (unitprice.is_null() ? 0 : unitprice.as<float>());}
        int getPu() { return pu; }
        void setDay(string d) { recordDate = d; }
        string getDay() { return recordDate; }
};


vector<PortfolioRecord> getPortfolioRecords(pqxx::result R) {
   vector<PortfolioRecord> records;
   for (result::const_iterator c = R.begin(); c != R.end(); ++c) {
      PortfolioRecord record;
      record.setActif(c[0].as<string>());
      record.setPu(c[1]);
      record.setDay(c[2].as<string>());
      records.push_back(record);
      cout << "actif = " << record.getActif() << endl;
      cout << "pu = " << record.getPu() << endl;
      cout << "day = " << record.getDay() << endl;
   }
   return records;
};


int main(int argc, char* argv[]) {
   try {
      string connectionString = "dbname = dbt user = dbtprod password = " + to_string(getenv("DBT_PASSWORD")) + " hostaddr = 0.0.0.0 port = 5432";
      connection C(connectionString);
      if (C.is_open()) {
         cout << "Opened database successfully: " << C.dbname() << endl;
         const string sql  = "SELECT actif, pu, day from details order by day asc ";
         nontransaction N(C);
         result R( N.exec( sql ));
         getPortfolioRecords(R);

      }
     else {
         cout << "Can't open database" << endl;
         return 1;
      }
      C.disconnect ();
   } catch (const std::exception &e) {
      cerr << e.what() << std::endl;
      return 1;
   }
}
