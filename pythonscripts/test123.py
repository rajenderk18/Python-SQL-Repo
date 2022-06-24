import datetime
import time

d = datetime.datetime.utcnow()
print (d, d.hour-4)
print(time.gmtime().tm_hour)
if d.hour > 10:
        print ("Run your code here")

configuration = global_function_2();
instanceJson = context.get("instance");
portalID = instanceJson.get("id");
workorderid = requestObj.get('id');
template_name = requestObj.get("template").get("name");
picklist = requestObj.get('udf_fields').get('udf_pick_100000001');
approvalJson = Collection();
approvalStages = Collection();
if (template_name == "Paper Check Request Form" & & (!"null".equals(picklist)))
{

if ("1100H 519 Health & Welfare Fund".equals(picklist))
{
    new_group = "Accounting";
approver = "osuarez@neba-fl.com";
technician = "Felix Mendoza";}

else if ("1125H UFCW Med-1000".equals(picklist)) {
new_group = "Accounting";
approver = "cruiz@neba-fl.com";
technician = "Felix Mendoza";}

else if ("1130H UFCW Local 1000 Oklahoma H & W".equals(picklist)) {
new_group = "Accounting";
approver = "cruiz@neba-fl.com";
technician = "Felix Mendoza";}

else if ("1135H UFCW Local 1625 H&W Fund".equals(picklist)) {
new_group = "Accounting";
approver = "osuarez@neba-fl.com";
technician = "Felix Mendoza";}

else if ("1140H UFCW Allied Trades Trust Fund".equals(picklist)) {
new_group = "Accounting";
approver = "nroman@neba-fl.com";
technician = "Felix Mendoza";}

else if ("1145H South Florida Hotel & Culinary".equals(picklist)) {
new_group = "Accounting";
approver = "nroman@neba-fl.com";
technician = "Felix Mendoza";}

else if ("1155H Tampa Banana Handlers Welfare".equals(picklist)) {
new_group = "Accounting";
approver = "vmonsalve@neba-fl.com";
technician = "Felix Mendoza";}

else if ("1160H Sheetmetal Workers LU 32 H&W".equals(picklist)) {
new_group = "Accounting";
approver = "nroman@neba-fl.com";
technician = "Felix Mendoza";}

else if ("1180H UA Plumbers 421 H & W Fund".equals(picklist)) {
new_group = "Accounting";
approver = "tshouse@neba-fl.com";
technician = "Felix Mendoza";}

else if ("1185H IBEW Local 728 Healthcare Plan".equals(picklist)) {
new_group = "Accounting";
approver = "vmonsalve@neba-fl.com";
technician = "Felix Mendoza";}

else if ("1190H P&P LU 719 Welfare Fund".equals(picklist)) {
new_group = "Accounting";
approver = "nroman@neba-fl.com";
technician = "Felix Mendoza";}

else if ("1200H Atl P&S Local 72 H&W Fund".equals(picklist)) {
new_group = "Accounting";
approver = "etaylor@neba-fl.com";
technician = "Felix Mendoza";}

else if ("1200HR Atl P&S Local 72 Retiree H&W".equals(picklist)) {
new_group = "Accounting";
approver = "etaylor@neba-fl.com";
technician = "Felix Mendoza";}

else if ("1210H UFCW KC Health & Welfare Fund".equals(picklist)) {
new_group = "Accounting";
approver = "tshouse@neba-fl.com";
technician = "Felix Mendoza";}

else if ("1230H Tampa".equals(picklist)) {
new_group = "Accounting";
approver = "slantigua@neba-fl.com";
technician = "Felix Mendoza";}

else if ("1240H SM20 Fund".equals(picklist)) {
new_group = "Accounting";
approver = "fmendoza@neba-fl.com";
technician = "Felix Mendoza";}

else if ("1250H NAW Welfare".equals(picklist)) {
new_group = "Accounting";
approver = "vmonsalve@neba-fl.com";
technician = "Felix Mendoza";}

else if ("2210H 123 Health & Welfare Fund".equals(picklist)) {
new_group = "Retirement Claims";
approver = "smartin@neba-fl.com";
technician = "Robert Wright";}

else if ("2220H Plumbers 295 Health & Welfare Fund".equals(picklist)) {
new_group = "Retirement Claims";
approver = "smartin@neba-fl.com";
technician = "Robert Wright";}

else if ("2240H Plumbers 803 Health & Welfare Fund".equals(picklist)) {
new_group = "Accounting";
approver = "smartin@neba-fl.com";
technician = "Robert Wright";}

else if ("2270H 188 Health & Welfare".equals(picklist)) {
new_group = "Retirement Claims";
approver = "smartin@neba-fl.com";
technician = "Robert Wright";}

else if ("2280H 198 Health & Welfare Fund".equals(picklist)) {
new_group = "Retirement Claims";
approver = "slantigua@neba-fl.com";
technician = "Robert Wright";}

else if ("3120H P&P LU 630 Welfare Fund".equals(picklist)) {
new_group = "Accounting";
approver = "eceast@neba-fl.com";
technician = "Felix Mendoza";}

else if ("4100H IBEW Local 613 Health Plan".equals(picklist)) {
new_group = "Accounting";
approver = "vmonsalve@neba-fl.com";
technician = "Felix Mendoza";}

else if ("4100HR IBEW Local 613 Retiree Health".equals(picklist)) {
new_group = "Accounting";
approver = "vmonsalve@neba-fl.com";
technician = "Felix Mendoza";}

else if ("4105H IBEW Local 508 Health Plan".equals(picklist)) {
new_group = "Retirement Claims";
approver = "ewetmore@neba-fl.com";
technician = "Robert Wright";}

else {
new_group = "Accounting";
approver = "rburnley@neba-fl.com";
technician = "Felix Mendoza";}
}
else {
returnJson = {"result":"Failed", "message": "Template name not matched"};
}
if (!"null".equals(technician) & & !"null".equals(approver))
{
    url = configuration.get('url') + "/api/v3/requests/" + workorderid;
headers = {"authtoken": configuration.get("technicianKey"), "portalid": portalID};
input_data = {"request": {"technician": {"name": technician},
                          "group": {"name": new_group}}};
// info
input_data;
response = invokeurl
[
           url: url
type: PUT
parameters: {"input_data": input_data}
headers: headers
];
// info
response;
if (response.get('response_status').get('status') == 'success')
{

    taskurl = configuration.get("url") + "/api/v3/tasks";
input_data = {
    "task": {"title": "New task added " + picklist,
             "description": "New task added " + picklist,
             "status": {"name": "Open"},
             "owner": {"email_id": approver},
             "request": {"id": workorderid}}};
// info
input_data;
params = {"input_data": input_data};
response = invokeurl
[
           url: taskurl
type: POST
parameters: params
headers: headers
];
if (response.get("response_status").get("status") == 'success'){
stage1 = {"StageOne":[approver]};
approvalStages.insert(stage1);
approvalJson.insert("approval_stages": approvalStages);
approvalStages = approvalJson.get("approval_stages");
input_data = {"INPUT_DATA": approvalStages, "OPERATIONNAME": "SET_APPROVAL_STAGE", "send_immediately": "True"};
operations = Collection();
operations.insert(input_data);
returnJson = {"operation": operations, "message": "Approval(S) added Successfully through Custom Trigger",
              "result": "success"};
}
}
}

else {
    returnJson = {"result": "success", "message": "No Approval(s) set through the Script"};
}

// info
returnJson;
return returnJson;
