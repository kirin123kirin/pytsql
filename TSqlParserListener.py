# Generated from TSqlParser.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TSqlParser import TSqlParser
else:
    from TSqlParser import TSqlParser

# This class defines a complete listener for a parse tree produced by TSqlParser.
class TSqlParserListener(ParseTreeListener):
	
    # Enter a parse tree produced by TSqlParser#tsql_file.
    def enterTsql_file(self, ctx:TSqlParser.Tsql_fileContext):
        pass

    # Exit a parse tree produced by TSqlParser#tsql_file.
    def exitTsql_file(self, ctx:TSqlParser.Tsql_fileContext):
        pass


    # Enter a parse tree produced by TSqlParser#batch.
    def enterBatch(self, ctx:TSqlParser.BatchContext):
        pass

    # Exit a parse tree produced by TSqlParser#batch.
    def exitBatch(self, ctx:TSqlParser.BatchContext):
        pass


    # Enter a parse tree produced by TSqlParser#sql_clauses.
    def enterSql_clauses(self, ctx:TSqlParser.Sql_clausesContext):
        pass

    # Exit a parse tree produced by TSqlParser#sql_clauses.
    def exitSql_clauses(self, ctx:TSqlParser.Sql_clausesContext):
        pass


    # Enter a parse tree produced by TSqlParser#sql_clause.
    def enterSql_clause(self, ctx:TSqlParser.Sql_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#sql_clause.
    def exitSql_clause(self, ctx:TSqlParser.Sql_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#dml_clause.
    def enterDml_clause(self, ctx:TSqlParser.Dml_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#dml_clause.
    def exitDml_clause(self, ctx:TSqlParser.Dml_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#ddl_clause.
    def enterDdl_clause(self, ctx:TSqlParser.Ddl_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#ddl_clause.
    def exitDdl_clause(self, ctx:TSqlParser.Ddl_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#backup_statement.
    def enterBackup_statement(self, ctx:TSqlParser.Backup_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#backup_statement.
    def exitBackup_statement(self, ctx:TSqlParser.Backup_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#cfl_statement.
    def enterCfl_statement(self, ctx:TSqlParser.Cfl_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#cfl_statement.
    def exitCfl_statement(self, ctx:TSqlParser.Cfl_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#block_statement.
    def enterBlock_statement(self, ctx:TSqlParser.Block_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#block_statement.
    def exitBlock_statement(self, ctx:TSqlParser.Block_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#break_statement.
    def enterBreak_statement(self, ctx:TSqlParser.Break_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#break_statement.
    def exitBreak_statement(self, ctx:TSqlParser.Break_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#continue_statement.
    def enterContinue_statement(self, ctx:TSqlParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#continue_statement.
    def exitContinue_statement(self, ctx:TSqlParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#goto_statement.
    def enterGoto_statement(self, ctx:TSqlParser.Goto_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#goto_statement.
    def exitGoto_statement(self, ctx:TSqlParser.Goto_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#return_statement.
    def enterReturn_statement(self, ctx:TSqlParser.Return_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#return_statement.
    def exitReturn_statement(self, ctx:TSqlParser.Return_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#if_statement.
    def enterIf_statement(self, ctx:TSqlParser.If_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#if_statement.
    def exitIf_statement(self, ctx:TSqlParser.If_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#throw_statement.
    def enterThrow_statement(self, ctx:TSqlParser.Throw_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#throw_statement.
    def exitThrow_statement(self, ctx:TSqlParser.Throw_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#throw_error_number.
    def enterThrow_error_number(self, ctx:TSqlParser.Throw_error_numberContext):
        pass

    # Exit a parse tree produced by TSqlParser#throw_error_number.
    def exitThrow_error_number(self, ctx:TSqlParser.Throw_error_numberContext):
        pass


    # Enter a parse tree produced by TSqlParser#throw_message.
    def enterThrow_message(self, ctx:TSqlParser.Throw_messageContext):
        pass

    # Exit a parse tree produced by TSqlParser#throw_message.
    def exitThrow_message(self, ctx:TSqlParser.Throw_messageContext):
        pass


    # Enter a parse tree produced by TSqlParser#throw_state.
    def enterThrow_state(self, ctx:TSqlParser.Throw_stateContext):
        pass

    # Exit a parse tree produced by TSqlParser#throw_state.
    def exitThrow_state(self, ctx:TSqlParser.Throw_stateContext):
        pass


    # Enter a parse tree produced by TSqlParser#try_catch_statement.
    def enterTry_catch_statement(self, ctx:TSqlParser.Try_catch_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#try_catch_statement.
    def exitTry_catch_statement(self, ctx:TSqlParser.Try_catch_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#waitfor_statement.
    def enterWaitfor_statement(self, ctx:TSqlParser.Waitfor_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#waitfor_statement.
    def exitWaitfor_statement(self, ctx:TSqlParser.Waitfor_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#while_statement.
    def enterWhile_statement(self, ctx:TSqlParser.While_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#while_statement.
    def exitWhile_statement(self, ctx:TSqlParser.While_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#print_statement.
    def enterPrint_statement(self, ctx:TSqlParser.Print_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#print_statement.
    def exitPrint_statement(self, ctx:TSqlParser.Print_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#raiseerror_statement.
    def enterRaiseerror_statement(self, ctx:TSqlParser.Raiseerror_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#raiseerror_statement.
    def exitRaiseerror_statement(self, ctx:TSqlParser.Raiseerror_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#empty_statement.
    def enterEmpty_statement(self, ctx:TSqlParser.Empty_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#empty_statement.
    def exitEmpty_statement(self, ctx:TSqlParser.Empty_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#another_statement.
    def enterAnother_statement(self, ctx:TSqlParser.Another_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#another_statement.
    def exitAnother_statement(self, ctx:TSqlParser.Another_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_application_role.
    def enterAlter_application_role(self, ctx:TSqlParser.Alter_application_roleContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_application_role.
    def exitAlter_application_role(self, ctx:TSqlParser.Alter_application_roleContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_application_role.
    def enterCreate_application_role(self, ctx:TSqlParser.Create_application_roleContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_application_role.
    def exitCreate_application_role(self, ctx:TSqlParser.Create_application_roleContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_aggregate.
    def enterDrop_aggregate(self, ctx:TSqlParser.Drop_aggregateContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_aggregate.
    def exitDrop_aggregate(self, ctx:TSqlParser.Drop_aggregateContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_application_role.
    def enterDrop_application_role(self, ctx:TSqlParser.Drop_application_roleContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_application_role.
    def exitDrop_application_role(self, ctx:TSqlParser.Drop_application_roleContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_assembly.
    def enterAlter_assembly(self, ctx:TSqlParser.Alter_assemblyContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_assembly.
    def exitAlter_assembly(self, ctx:TSqlParser.Alter_assemblyContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_assembly_start.
    def enterAlter_assembly_start(self, ctx:TSqlParser.Alter_assembly_startContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_assembly_start.
    def exitAlter_assembly_start(self, ctx:TSqlParser.Alter_assembly_startContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_assembly_clause.
    def enterAlter_assembly_clause(self, ctx:TSqlParser.Alter_assembly_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_assembly_clause.
    def exitAlter_assembly_clause(self, ctx:TSqlParser.Alter_assembly_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_assembly_from_clause.
    def enterAlter_assembly_from_clause(self, ctx:TSqlParser.Alter_assembly_from_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_assembly_from_clause.
    def exitAlter_assembly_from_clause(self, ctx:TSqlParser.Alter_assembly_from_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_assembly_from_clause_start.
    def enterAlter_assembly_from_clause_start(self, ctx:TSqlParser.Alter_assembly_from_clause_startContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_assembly_from_clause_start.
    def exitAlter_assembly_from_clause_start(self, ctx:TSqlParser.Alter_assembly_from_clause_startContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_assembly_drop_clause.
    def enterAlter_assembly_drop_clause(self, ctx:TSqlParser.Alter_assembly_drop_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_assembly_drop_clause.
    def exitAlter_assembly_drop_clause(self, ctx:TSqlParser.Alter_assembly_drop_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_assembly_drop_multiple_files.
    def enterAlter_assembly_drop_multiple_files(self, ctx:TSqlParser.Alter_assembly_drop_multiple_filesContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_assembly_drop_multiple_files.
    def exitAlter_assembly_drop_multiple_files(self, ctx:TSqlParser.Alter_assembly_drop_multiple_filesContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_assembly_drop.
    def enterAlter_assembly_drop(self, ctx:TSqlParser.Alter_assembly_dropContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_assembly_drop.
    def exitAlter_assembly_drop(self, ctx:TSqlParser.Alter_assembly_dropContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_assembly_add_clause.
    def enterAlter_assembly_add_clause(self, ctx:TSqlParser.Alter_assembly_add_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_assembly_add_clause.
    def exitAlter_assembly_add_clause(self, ctx:TSqlParser.Alter_assembly_add_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_asssembly_add_clause_start.
    def enterAlter_asssembly_add_clause_start(self, ctx:TSqlParser.Alter_asssembly_add_clause_startContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_asssembly_add_clause_start.
    def exitAlter_asssembly_add_clause_start(self, ctx:TSqlParser.Alter_asssembly_add_clause_startContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_assembly_client_file_clause.
    def enterAlter_assembly_client_file_clause(self, ctx:TSqlParser.Alter_assembly_client_file_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_assembly_client_file_clause.
    def exitAlter_assembly_client_file_clause(self, ctx:TSqlParser.Alter_assembly_client_file_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_assembly_file_name.
    def enterAlter_assembly_file_name(self, ctx:TSqlParser.Alter_assembly_file_nameContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_assembly_file_name.
    def exitAlter_assembly_file_name(self, ctx:TSqlParser.Alter_assembly_file_nameContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_assembly_file_bits.
    def enterAlter_assembly_file_bits(self, ctx:TSqlParser.Alter_assembly_file_bitsContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_assembly_file_bits.
    def exitAlter_assembly_file_bits(self, ctx:TSqlParser.Alter_assembly_file_bitsContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_assembly_as.
    def enterAlter_assembly_as(self, ctx:TSqlParser.Alter_assembly_asContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_assembly_as.
    def exitAlter_assembly_as(self, ctx:TSqlParser.Alter_assembly_asContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_assembly_with_clause.
    def enterAlter_assembly_with_clause(self, ctx:TSqlParser.Alter_assembly_with_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_assembly_with_clause.
    def exitAlter_assembly_with_clause(self, ctx:TSqlParser.Alter_assembly_with_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_assembly_with.
    def enterAlter_assembly_with(self, ctx:TSqlParser.Alter_assembly_withContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_assembly_with.
    def exitAlter_assembly_with(self, ctx:TSqlParser.Alter_assembly_withContext):
        pass


    # Enter a parse tree produced by TSqlParser#client_assembly_specifier.
    def enterClient_assembly_specifier(self, ctx:TSqlParser.Client_assembly_specifierContext):
        pass

    # Exit a parse tree produced by TSqlParser#client_assembly_specifier.
    def exitClient_assembly_specifier(self, ctx:TSqlParser.Client_assembly_specifierContext):
        pass


    # Enter a parse tree produced by TSqlParser#assembly_option.
    def enterAssembly_option(self, ctx:TSqlParser.Assembly_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#assembly_option.
    def exitAssembly_option(self, ctx:TSqlParser.Assembly_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#network_file_share.
    def enterNetwork_file_share(self, ctx:TSqlParser.Network_file_shareContext):
        pass

    # Exit a parse tree produced by TSqlParser#network_file_share.
    def exitNetwork_file_share(self, ctx:TSqlParser.Network_file_shareContext):
        pass


    # Enter a parse tree produced by TSqlParser#network_computer.
    def enterNetwork_computer(self, ctx:TSqlParser.Network_computerContext):
        pass

    # Exit a parse tree produced by TSqlParser#network_computer.
    def exitNetwork_computer(self, ctx:TSqlParser.Network_computerContext):
        pass


    # Enter a parse tree produced by TSqlParser#network_file_start.
    def enterNetwork_file_start(self, ctx:TSqlParser.Network_file_startContext):
        pass

    # Exit a parse tree produced by TSqlParser#network_file_start.
    def exitNetwork_file_start(self, ctx:TSqlParser.Network_file_startContext):
        pass


    # Enter a parse tree produced by TSqlParser#file_path.
    def enterFile_path(self, ctx:TSqlParser.File_pathContext):
        pass

    # Exit a parse tree produced by TSqlParser#file_path.
    def exitFile_path(self, ctx:TSqlParser.File_pathContext):
        pass


    # Enter a parse tree produced by TSqlParser#file_directory_path_separator.
    def enterFile_directory_path_separator(self, ctx:TSqlParser.File_directory_path_separatorContext):
        pass

    # Exit a parse tree produced by TSqlParser#file_directory_path_separator.
    def exitFile_directory_path_separator(self, ctx:TSqlParser.File_directory_path_separatorContext):
        pass


    # Enter a parse tree produced by TSqlParser#local_file.
    def enterLocal_file(self, ctx:TSqlParser.Local_fileContext):
        pass

    # Exit a parse tree produced by TSqlParser#local_file.
    def exitLocal_file(self, ctx:TSqlParser.Local_fileContext):
        pass


    # Enter a parse tree produced by TSqlParser#local_drive.
    def enterLocal_drive(self, ctx:TSqlParser.Local_driveContext):
        pass

    # Exit a parse tree produced by TSqlParser#local_drive.
    def exitLocal_drive(self, ctx:TSqlParser.Local_driveContext):
        pass


    # Enter a parse tree produced by TSqlParser#multiple_local_files.
    def enterMultiple_local_files(self, ctx:TSqlParser.Multiple_local_filesContext):
        pass

    # Exit a parse tree produced by TSqlParser#multiple_local_files.
    def exitMultiple_local_files(self, ctx:TSqlParser.Multiple_local_filesContext):
        pass


    # Enter a parse tree produced by TSqlParser#multiple_local_file_start.
    def enterMultiple_local_file_start(self, ctx:TSqlParser.Multiple_local_file_startContext):
        pass

    # Exit a parse tree produced by TSqlParser#multiple_local_file_start.
    def exitMultiple_local_file_start(self, ctx:TSqlParser.Multiple_local_file_startContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_assembly.
    def enterCreate_assembly(self, ctx:TSqlParser.Create_assemblyContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_assembly.
    def exitCreate_assembly(self, ctx:TSqlParser.Create_assemblyContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_assembly.
    def enterDrop_assembly(self, ctx:TSqlParser.Drop_assemblyContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_assembly.
    def exitDrop_assembly(self, ctx:TSqlParser.Drop_assemblyContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_asymmetric_key.
    def enterAlter_asymmetric_key(self, ctx:TSqlParser.Alter_asymmetric_keyContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_asymmetric_key.
    def exitAlter_asymmetric_key(self, ctx:TSqlParser.Alter_asymmetric_keyContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_asymmetric_key_start.
    def enterAlter_asymmetric_key_start(self, ctx:TSqlParser.Alter_asymmetric_key_startContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_asymmetric_key_start.
    def exitAlter_asymmetric_key_start(self, ctx:TSqlParser.Alter_asymmetric_key_startContext):
        pass


    # Enter a parse tree produced by TSqlParser#asymmetric_key_option.
    def enterAsymmetric_key_option(self, ctx:TSqlParser.Asymmetric_key_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#asymmetric_key_option.
    def exitAsymmetric_key_option(self, ctx:TSqlParser.Asymmetric_key_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#asymmetric_key_option_start.
    def enterAsymmetric_key_option_start(self, ctx:TSqlParser.Asymmetric_key_option_startContext):
        pass

    # Exit a parse tree produced by TSqlParser#asymmetric_key_option_start.
    def exitAsymmetric_key_option_start(self, ctx:TSqlParser.Asymmetric_key_option_startContext):
        pass


    # Enter a parse tree produced by TSqlParser#asymmetric_key_password_change_option.
    def enterAsymmetric_key_password_change_option(self, ctx:TSqlParser.Asymmetric_key_password_change_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#asymmetric_key_password_change_option.
    def exitAsymmetric_key_password_change_option(self, ctx:TSqlParser.Asymmetric_key_password_change_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_asymmetric_key.
    def enterCreate_asymmetric_key(self, ctx:TSqlParser.Create_asymmetric_keyContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_asymmetric_key.
    def exitCreate_asymmetric_key(self, ctx:TSqlParser.Create_asymmetric_keyContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_asymmetric_key.
    def enterDrop_asymmetric_key(self, ctx:TSqlParser.Drop_asymmetric_keyContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_asymmetric_key.
    def exitDrop_asymmetric_key(self, ctx:TSqlParser.Drop_asymmetric_keyContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_authorization.
    def enterAlter_authorization(self, ctx:TSqlParser.Alter_authorizationContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_authorization.
    def exitAlter_authorization(self, ctx:TSqlParser.Alter_authorizationContext):
        pass


    # Enter a parse tree produced by TSqlParser#authorization_grantee.
    def enterAuthorization_grantee(self, ctx:TSqlParser.Authorization_granteeContext):
        pass

    # Exit a parse tree produced by TSqlParser#authorization_grantee.
    def exitAuthorization_grantee(self, ctx:TSqlParser.Authorization_granteeContext):
        pass


    # Enter a parse tree produced by TSqlParser#entity_to.
    def enterEntity_to(self, ctx:TSqlParser.Entity_toContext):
        pass

    # Exit a parse tree produced by TSqlParser#entity_to.
    def exitEntity_to(self, ctx:TSqlParser.Entity_toContext):
        pass


    # Enter a parse tree produced by TSqlParser#colon_colon.
    def enterColon_colon(self, ctx:TSqlParser.Colon_colonContext):
        pass

    # Exit a parse tree produced by TSqlParser#colon_colon.
    def exitColon_colon(self, ctx:TSqlParser.Colon_colonContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_authorization_start.
    def enterAlter_authorization_start(self, ctx:TSqlParser.Alter_authorization_startContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_authorization_start.
    def exitAlter_authorization_start(self, ctx:TSqlParser.Alter_authorization_startContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_authorization_for_sql_database.
    def enterAlter_authorization_for_sql_database(self, ctx:TSqlParser.Alter_authorization_for_sql_databaseContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_authorization_for_sql_database.
    def exitAlter_authorization_for_sql_database(self, ctx:TSqlParser.Alter_authorization_for_sql_databaseContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_authorization_for_azure_dw.
    def enterAlter_authorization_for_azure_dw(self, ctx:TSqlParser.Alter_authorization_for_azure_dwContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_authorization_for_azure_dw.
    def exitAlter_authorization_for_azure_dw(self, ctx:TSqlParser.Alter_authorization_for_azure_dwContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_authorization_for_parallel_dw.
    def enterAlter_authorization_for_parallel_dw(self, ctx:TSqlParser.Alter_authorization_for_parallel_dwContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_authorization_for_parallel_dw.
    def exitAlter_authorization_for_parallel_dw(self, ctx:TSqlParser.Alter_authorization_for_parallel_dwContext):
        pass


    # Enter a parse tree produced by TSqlParser#class_type.
    def enterClass_type(self, ctx:TSqlParser.Class_typeContext):
        pass

    # Exit a parse tree produced by TSqlParser#class_type.
    def exitClass_type(self, ctx:TSqlParser.Class_typeContext):
        pass


    # Enter a parse tree produced by TSqlParser#class_type_for_sql_database.
    def enterClass_type_for_sql_database(self, ctx:TSqlParser.Class_type_for_sql_databaseContext):
        pass

    # Exit a parse tree produced by TSqlParser#class_type_for_sql_database.
    def exitClass_type_for_sql_database(self, ctx:TSqlParser.Class_type_for_sql_databaseContext):
        pass


    # Enter a parse tree produced by TSqlParser#class_type_for_azure_dw.
    def enterClass_type_for_azure_dw(self, ctx:TSqlParser.Class_type_for_azure_dwContext):
        pass

    # Exit a parse tree produced by TSqlParser#class_type_for_azure_dw.
    def exitClass_type_for_azure_dw(self, ctx:TSqlParser.Class_type_for_azure_dwContext):
        pass


    # Enter a parse tree produced by TSqlParser#class_type_for_parallel_dw.
    def enterClass_type_for_parallel_dw(self, ctx:TSqlParser.Class_type_for_parallel_dwContext):
        pass

    # Exit a parse tree produced by TSqlParser#class_type_for_parallel_dw.
    def exitClass_type_for_parallel_dw(self, ctx:TSqlParser.Class_type_for_parallel_dwContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_availability_group.
    def enterDrop_availability_group(self, ctx:TSqlParser.Drop_availability_groupContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_availability_group.
    def exitDrop_availability_group(self, ctx:TSqlParser.Drop_availability_groupContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_availability_group.
    def enterAlter_availability_group(self, ctx:TSqlParser.Alter_availability_groupContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_availability_group.
    def exitAlter_availability_group(self, ctx:TSqlParser.Alter_availability_groupContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_availability_group_start.
    def enterAlter_availability_group_start(self, ctx:TSqlParser.Alter_availability_group_startContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_availability_group_start.
    def exitAlter_availability_group_start(self, ctx:TSqlParser.Alter_availability_group_startContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_availability_group_options.
    def enterAlter_availability_group_options(self, ctx:TSqlParser.Alter_availability_group_optionsContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_availability_group_options.
    def exitAlter_availability_group_options(self, ctx:TSqlParser.Alter_availability_group_optionsContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_or_alter_broker_priority.
    def enterCreate_or_alter_broker_priority(self, ctx:TSqlParser.Create_or_alter_broker_priorityContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_or_alter_broker_priority.
    def exitCreate_or_alter_broker_priority(self, ctx:TSqlParser.Create_or_alter_broker_priorityContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_broker_priority.
    def enterDrop_broker_priority(self, ctx:TSqlParser.Drop_broker_priorityContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_broker_priority.
    def exitDrop_broker_priority(self, ctx:TSqlParser.Drop_broker_priorityContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_certificate.
    def enterAlter_certificate(self, ctx:TSqlParser.Alter_certificateContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_certificate.
    def exitAlter_certificate(self, ctx:TSqlParser.Alter_certificateContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_column_encryption_key.
    def enterAlter_column_encryption_key(self, ctx:TSqlParser.Alter_column_encryption_keyContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_column_encryption_key.
    def exitAlter_column_encryption_key(self, ctx:TSqlParser.Alter_column_encryption_keyContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_column_encryption_key.
    def enterCreate_column_encryption_key(self, ctx:TSqlParser.Create_column_encryption_keyContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_column_encryption_key.
    def exitCreate_column_encryption_key(self, ctx:TSqlParser.Create_column_encryption_keyContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_certificate.
    def enterDrop_certificate(self, ctx:TSqlParser.Drop_certificateContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_certificate.
    def exitDrop_certificate(self, ctx:TSqlParser.Drop_certificateContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_column_encryption_key.
    def enterDrop_column_encryption_key(self, ctx:TSqlParser.Drop_column_encryption_keyContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_column_encryption_key.
    def exitDrop_column_encryption_key(self, ctx:TSqlParser.Drop_column_encryption_keyContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_column_master_key.
    def enterDrop_column_master_key(self, ctx:TSqlParser.Drop_column_master_keyContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_column_master_key.
    def exitDrop_column_master_key(self, ctx:TSqlParser.Drop_column_master_keyContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_contract.
    def enterDrop_contract(self, ctx:TSqlParser.Drop_contractContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_contract.
    def exitDrop_contract(self, ctx:TSqlParser.Drop_contractContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_credential.
    def enterDrop_credential(self, ctx:TSqlParser.Drop_credentialContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_credential.
    def exitDrop_credential(self, ctx:TSqlParser.Drop_credentialContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_cryptograhic_provider.
    def enterDrop_cryptograhic_provider(self, ctx:TSqlParser.Drop_cryptograhic_providerContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_cryptograhic_provider.
    def exitDrop_cryptograhic_provider(self, ctx:TSqlParser.Drop_cryptograhic_providerContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_database.
    def enterDrop_database(self, ctx:TSqlParser.Drop_databaseContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_database.
    def exitDrop_database(self, ctx:TSqlParser.Drop_databaseContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_database_audit_specification.
    def enterDrop_database_audit_specification(self, ctx:TSqlParser.Drop_database_audit_specificationContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_database_audit_specification.
    def exitDrop_database_audit_specification(self, ctx:TSqlParser.Drop_database_audit_specificationContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_database_scoped_credential.
    def enterDrop_database_scoped_credential(self, ctx:TSqlParser.Drop_database_scoped_credentialContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_database_scoped_credential.
    def exitDrop_database_scoped_credential(self, ctx:TSqlParser.Drop_database_scoped_credentialContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_default.
    def enterDrop_default(self, ctx:TSqlParser.Drop_defaultContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_default.
    def exitDrop_default(self, ctx:TSqlParser.Drop_defaultContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_endpoint.
    def enterDrop_endpoint(self, ctx:TSqlParser.Drop_endpointContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_endpoint.
    def exitDrop_endpoint(self, ctx:TSqlParser.Drop_endpointContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_external_data_source.
    def enterDrop_external_data_source(self, ctx:TSqlParser.Drop_external_data_sourceContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_external_data_source.
    def exitDrop_external_data_source(self, ctx:TSqlParser.Drop_external_data_sourceContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_external_file_format.
    def enterDrop_external_file_format(self, ctx:TSqlParser.Drop_external_file_formatContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_external_file_format.
    def exitDrop_external_file_format(self, ctx:TSqlParser.Drop_external_file_formatContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_external_library.
    def enterDrop_external_library(self, ctx:TSqlParser.Drop_external_libraryContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_external_library.
    def exitDrop_external_library(self, ctx:TSqlParser.Drop_external_libraryContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_external_resource_pool.
    def enterDrop_external_resource_pool(self, ctx:TSqlParser.Drop_external_resource_poolContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_external_resource_pool.
    def exitDrop_external_resource_pool(self, ctx:TSqlParser.Drop_external_resource_poolContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_external_table.
    def enterDrop_external_table(self, ctx:TSqlParser.Drop_external_tableContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_external_table.
    def exitDrop_external_table(self, ctx:TSqlParser.Drop_external_tableContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_event_notifications.
    def enterDrop_event_notifications(self, ctx:TSqlParser.Drop_event_notificationsContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_event_notifications.
    def exitDrop_event_notifications(self, ctx:TSqlParser.Drop_event_notificationsContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_event_session.
    def enterDrop_event_session(self, ctx:TSqlParser.Drop_event_sessionContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_event_session.
    def exitDrop_event_session(self, ctx:TSqlParser.Drop_event_sessionContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_fulltext_catalog.
    def enterDrop_fulltext_catalog(self, ctx:TSqlParser.Drop_fulltext_catalogContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_fulltext_catalog.
    def exitDrop_fulltext_catalog(self, ctx:TSqlParser.Drop_fulltext_catalogContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_fulltext_index.
    def enterDrop_fulltext_index(self, ctx:TSqlParser.Drop_fulltext_indexContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_fulltext_index.
    def exitDrop_fulltext_index(self, ctx:TSqlParser.Drop_fulltext_indexContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_fulltext_stoplist.
    def enterDrop_fulltext_stoplist(self, ctx:TSqlParser.Drop_fulltext_stoplistContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_fulltext_stoplist.
    def exitDrop_fulltext_stoplist(self, ctx:TSqlParser.Drop_fulltext_stoplistContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_login.
    def enterDrop_login(self, ctx:TSqlParser.Drop_loginContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_login.
    def exitDrop_login(self, ctx:TSqlParser.Drop_loginContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_master_key.
    def enterDrop_master_key(self, ctx:TSqlParser.Drop_master_keyContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_master_key.
    def exitDrop_master_key(self, ctx:TSqlParser.Drop_master_keyContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_message_type.
    def enterDrop_message_type(self, ctx:TSqlParser.Drop_message_typeContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_message_type.
    def exitDrop_message_type(self, ctx:TSqlParser.Drop_message_typeContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_partition_function.
    def enterDrop_partition_function(self, ctx:TSqlParser.Drop_partition_functionContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_partition_function.
    def exitDrop_partition_function(self, ctx:TSqlParser.Drop_partition_functionContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_partition_scheme.
    def enterDrop_partition_scheme(self, ctx:TSqlParser.Drop_partition_schemeContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_partition_scheme.
    def exitDrop_partition_scheme(self, ctx:TSqlParser.Drop_partition_schemeContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_queue.
    def enterDrop_queue(self, ctx:TSqlParser.Drop_queueContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_queue.
    def exitDrop_queue(self, ctx:TSqlParser.Drop_queueContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_remote_service_binding.
    def enterDrop_remote_service_binding(self, ctx:TSqlParser.Drop_remote_service_bindingContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_remote_service_binding.
    def exitDrop_remote_service_binding(self, ctx:TSqlParser.Drop_remote_service_bindingContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_resource_pool.
    def enterDrop_resource_pool(self, ctx:TSqlParser.Drop_resource_poolContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_resource_pool.
    def exitDrop_resource_pool(self, ctx:TSqlParser.Drop_resource_poolContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_db_role.
    def enterDrop_db_role(self, ctx:TSqlParser.Drop_db_roleContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_db_role.
    def exitDrop_db_role(self, ctx:TSqlParser.Drop_db_roleContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_route.
    def enterDrop_route(self, ctx:TSqlParser.Drop_routeContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_route.
    def exitDrop_route(self, ctx:TSqlParser.Drop_routeContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_rule.
    def enterDrop_rule(self, ctx:TSqlParser.Drop_ruleContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_rule.
    def exitDrop_rule(self, ctx:TSqlParser.Drop_ruleContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_schema.
    def enterDrop_schema(self, ctx:TSqlParser.Drop_schemaContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_schema.
    def exitDrop_schema(self, ctx:TSqlParser.Drop_schemaContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_search_property_list.
    def enterDrop_search_property_list(self, ctx:TSqlParser.Drop_search_property_listContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_search_property_list.
    def exitDrop_search_property_list(self, ctx:TSqlParser.Drop_search_property_listContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_security_policy.
    def enterDrop_security_policy(self, ctx:TSqlParser.Drop_security_policyContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_security_policy.
    def exitDrop_security_policy(self, ctx:TSqlParser.Drop_security_policyContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_sequence.
    def enterDrop_sequence(self, ctx:TSqlParser.Drop_sequenceContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_sequence.
    def exitDrop_sequence(self, ctx:TSqlParser.Drop_sequenceContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_server_audit.
    def enterDrop_server_audit(self, ctx:TSqlParser.Drop_server_auditContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_server_audit.
    def exitDrop_server_audit(self, ctx:TSqlParser.Drop_server_auditContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_server_audit_specification.
    def enterDrop_server_audit_specification(self, ctx:TSqlParser.Drop_server_audit_specificationContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_server_audit_specification.
    def exitDrop_server_audit_specification(self, ctx:TSqlParser.Drop_server_audit_specificationContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_server_role.
    def enterDrop_server_role(self, ctx:TSqlParser.Drop_server_roleContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_server_role.
    def exitDrop_server_role(self, ctx:TSqlParser.Drop_server_roleContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_service.
    def enterDrop_service(self, ctx:TSqlParser.Drop_serviceContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_service.
    def exitDrop_service(self, ctx:TSqlParser.Drop_serviceContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_signature.
    def enterDrop_signature(self, ctx:TSqlParser.Drop_signatureContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_signature.
    def exitDrop_signature(self, ctx:TSqlParser.Drop_signatureContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_statistics_name_azure_dw_and_pdw.
    def enterDrop_statistics_name_azure_dw_and_pdw(self, ctx:TSqlParser.Drop_statistics_name_azure_dw_and_pdwContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_statistics_name_azure_dw_and_pdw.
    def exitDrop_statistics_name_azure_dw_and_pdw(self, ctx:TSqlParser.Drop_statistics_name_azure_dw_and_pdwContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_symmetric_key.
    def enterDrop_symmetric_key(self, ctx:TSqlParser.Drop_symmetric_keyContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_symmetric_key.
    def exitDrop_symmetric_key(self, ctx:TSqlParser.Drop_symmetric_keyContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_synonym.
    def enterDrop_synonym(self, ctx:TSqlParser.Drop_synonymContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_synonym.
    def exitDrop_synonym(self, ctx:TSqlParser.Drop_synonymContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_user.
    def enterDrop_user(self, ctx:TSqlParser.Drop_userContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_user.
    def exitDrop_user(self, ctx:TSqlParser.Drop_userContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_workload_group.
    def enterDrop_workload_group(self, ctx:TSqlParser.Drop_workload_groupContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_workload_group.
    def exitDrop_workload_group(self, ctx:TSqlParser.Drop_workload_groupContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_xml_schema_collection.
    def enterDrop_xml_schema_collection(self, ctx:TSqlParser.Drop_xml_schema_collectionContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_xml_schema_collection.
    def exitDrop_xml_schema_collection(self, ctx:TSqlParser.Drop_xml_schema_collectionContext):
        pass


    # Enter a parse tree produced by TSqlParser#disable_trigger.
    def enterDisable_trigger(self, ctx:TSqlParser.Disable_triggerContext):
        pass

    # Exit a parse tree produced by TSqlParser#disable_trigger.
    def exitDisable_trigger(self, ctx:TSqlParser.Disable_triggerContext):
        pass


    # Enter a parse tree produced by TSqlParser#enable_trigger.
    def enterEnable_trigger(self, ctx:TSqlParser.Enable_triggerContext):
        pass

    # Exit a parse tree produced by TSqlParser#enable_trigger.
    def exitEnable_trigger(self, ctx:TSqlParser.Enable_triggerContext):
        pass


    # Enter a parse tree produced by TSqlParser#lock_table.
    def enterLock_table(self, ctx:TSqlParser.Lock_tableContext):
        pass

    # Exit a parse tree produced by TSqlParser#lock_table.
    def exitLock_table(self, ctx:TSqlParser.Lock_tableContext):
        pass


    # Enter a parse tree produced by TSqlParser#truncate_table.
    def enterTruncate_table(self, ctx:TSqlParser.Truncate_tableContext):
        pass

    # Exit a parse tree produced by TSqlParser#truncate_table.
    def exitTruncate_table(self, ctx:TSqlParser.Truncate_tableContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_column_master_key.
    def enterCreate_column_master_key(self, ctx:TSqlParser.Create_column_master_keyContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_column_master_key.
    def exitCreate_column_master_key(self, ctx:TSqlParser.Create_column_master_keyContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_credential.
    def enterAlter_credential(self, ctx:TSqlParser.Alter_credentialContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_credential.
    def exitAlter_credential(self, ctx:TSqlParser.Alter_credentialContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_credential.
    def enterCreate_credential(self, ctx:TSqlParser.Create_credentialContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_credential.
    def exitCreate_credential(self, ctx:TSqlParser.Create_credentialContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_cryptographic_provider.
    def enterAlter_cryptographic_provider(self, ctx:TSqlParser.Alter_cryptographic_providerContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_cryptographic_provider.
    def exitAlter_cryptographic_provider(self, ctx:TSqlParser.Alter_cryptographic_providerContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_cryptographic_provider.
    def enterCreate_cryptographic_provider(self, ctx:TSqlParser.Create_cryptographic_providerContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_cryptographic_provider.
    def exitCreate_cryptographic_provider(self, ctx:TSqlParser.Create_cryptographic_providerContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_event_notification.
    def enterCreate_event_notification(self, ctx:TSqlParser.Create_event_notificationContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_event_notification.
    def exitCreate_event_notification(self, ctx:TSqlParser.Create_event_notificationContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_or_alter_event_session.
    def enterCreate_or_alter_event_session(self, ctx:TSqlParser.Create_or_alter_event_sessionContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_or_alter_event_session.
    def exitCreate_or_alter_event_session(self, ctx:TSqlParser.Create_or_alter_event_sessionContext):
        pass


    # Enter a parse tree produced by TSqlParser#event_session_predicate_expression.
    def enterEvent_session_predicate_expression(self, ctx:TSqlParser.Event_session_predicate_expressionContext):
        pass

    # Exit a parse tree produced by TSqlParser#event_session_predicate_expression.
    def exitEvent_session_predicate_expression(self, ctx:TSqlParser.Event_session_predicate_expressionContext):
        pass


    # Enter a parse tree produced by TSqlParser#event_session_predicate_factor.
    def enterEvent_session_predicate_factor(self, ctx:TSqlParser.Event_session_predicate_factorContext):
        pass

    # Exit a parse tree produced by TSqlParser#event_session_predicate_factor.
    def exitEvent_session_predicate_factor(self, ctx:TSqlParser.Event_session_predicate_factorContext):
        pass


    # Enter a parse tree produced by TSqlParser#event_session_predicate_leaf.
    def enterEvent_session_predicate_leaf(self, ctx:TSqlParser.Event_session_predicate_leafContext):
        pass

    # Exit a parse tree produced by TSqlParser#event_session_predicate_leaf.
    def exitEvent_session_predicate_leaf(self, ctx:TSqlParser.Event_session_predicate_leafContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_external_data_source.
    def enterAlter_external_data_source(self, ctx:TSqlParser.Alter_external_data_sourceContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_external_data_source.
    def exitAlter_external_data_source(self, ctx:TSqlParser.Alter_external_data_sourceContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_external_library.
    def enterAlter_external_library(self, ctx:TSqlParser.Alter_external_libraryContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_external_library.
    def exitAlter_external_library(self, ctx:TSqlParser.Alter_external_libraryContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_external_library.
    def enterCreate_external_library(self, ctx:TSqlParser.Create_external_libraryContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_external_library.
    def exitCreate_external_library(self, ctx:TSqlParser.Create_external_libraryContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_external_resource_pool.
    def enterAlter_external_resource_pool(self, ctx:TSqlParser.Alter_external_resource_poolContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_external_resource_pool.
    def exitAlter_external_resource_pool(self, ctx:TSqlParser.Alter_external_resource_poolContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_external_resource_pool.
    def enterCreate_external_resource_pool(self, ctx:TSqlParser.Create_external_resource_poolContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_external_resource_pool.
    def exitCreate_external_resource_pool(self, ctx:TSqlParser.Create_external_resource_poolContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_fulltext_catalog.
    def enterAlter_fulltext_catalog(self, ctx:TSqlParser.Alter_fulltext_catalogContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_fulltext_catalog.
    def exitAlter_fulltext_catalog(self, ctx:TSqlParser.Alter_fulltext_catalogContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_fulltext_catalog.
    def enterCreate_fulltext_catalog(self, ctx:TSqlParser.Create_fulltext_catalogContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_fulltext_catalog.
    def exitCreate_fulltext_catalog(self, ctx:TSqlParser.Create_fulltext_catalogContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_fulltext_stoplist.
    def enterAlter_fulltext_stoplist(self, ctx:TSqlParser.Alter_fulltext_stoplistContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_fulltext_stoplist.
    def exitAlter_fulltext_stoplist(self, ctx:TSqlParser.Alter_fulltext_stoplistContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_fulltext_stoplist.
    def enterCreate_fulltext_stoplist(self, ctx:TSqlParser.Create_fulltext_stoplistContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_fulltext_stoplist.
    def exitCreate_fulltext_stoplist(self, ctx:TSqlParser.Create_fulltext_stoplistContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_login_sql_server.
    def enterAlter_login_sql_server(self, ctx:TSqlParser.Alter_login_sql_serverContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_login_sql_server.
    def exitAlter_login_sql_server(self, ctx:TSqlParser.Alter_login_sql_serverContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_login_sql_server.
    def enterCreate_login_sql_server(self, ctx:TSqlParser.Create_login_sql_serverContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_login_sql_server.
    def exitCreate_login_sql_server(self, ctx:TSqlParser.Create_login_sql_serverContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_login_azure_sql.
    def enterAlter_login_azure_sql(self, ctx:TSqlParser.Alter_login_azure_sqlContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_login_azure_sql.
    def exitAlter_login_azure_sql(self, ctx:TSqlParser.Alter_login_azure_sqlContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_login_azure_sql.
    def enterCreate_login_azure_sql(self, ctx:TSqlParser.Create_login_azure_sqlContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_login_azure_sql.
    def exitCreate_login_azure_sql(self, ctx:TSqlParser.Create_login_azure_sqlContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_login_azure_sql_dw_and_pdw.
    def enterAlter_login_azure_sql_dw_and_pdw(self, ctx:TSqlParser.Alter_login_azure_sql_dw_and_pdwContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_login_azure_sql_dw_and_pdw.
    def exitAlter_login_azure_sql_dw_and_pdw(self, ctx:TSqlParser.Alter_login_azure_sql_dw_and_pdwContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_login_pdw.
    def enterCreate_login_pdw(self, ctx:TSqlParser.Create_login_pdwContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_login_pdw.
    def exitCreate_login_pdw(self, ctx:TSqlParser.Create_login_pdwContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_master_key_sql_server.
    def enterAlter_master_key_sql_server(self, ctx:TSqlParser.Alter_master_key_sql_serverContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_master_key_sql_server.
    def exitAlter_master_key_sql_server(self, ctx:TSqlParser.Alter_master_key_sql_serverContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_master_key_sql_server.
    def enterCreate_master_key_sql_server(self, ctx:TSqlParser.Create_master_key_sql_serverContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_master_key_sql_server.
    def exitCreate_master_key_sql_server(self, ctx:TSqlParser.Create_master_key_sql_serverContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_master_key_azure_sql.
    def enterAlter_master_key_azure_sql(self, ctx:TSqlParser.Alter_master_key_azure_sqlContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_master_key_azure_sql.
    def exitAlter_master_key_azure_sql(self, ctx:TSqlParser.Alter_master_key_azure_sqlContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_master_key_azure_sql.
    def enterCreate_master_key_azure_sql(self, ctx:TSqlParser.Create_master_key_azure_sqlContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_master_key_azure_sql.
    def exitCreate_master_key_azure_sql(self, ctx:TSqlParser.Create_master_key_azure_sqlContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_message_type.
    def enterAlter_message_type(self, ctx:TSqlParser.Alter_message_typeContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_message_type.
    def exitAlter_message_type(self, ctx:TSqlParser.Alter_message_typeContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_partition_function.
    def enterAlter_partition_function(self, ctx:TSqlParser.Alter_partition_functionContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_partition_function.
    def exitAlter_partition_function(self, ctx:TSqlParser.Alter_partition_functionContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_partition_scheme.
    def enterAlter_partition_scheme(self, ctx:TSqlParser.Alter_partition_schemeContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_partition_scheme.
    def exitAlter_partition_scheme(self, ctx:TSqlParser.Alter_partition_schemeContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_remote_service_binding.
    def enterAlter_remote_service_binding(self, ctx:TSqlParser.Alter_remote_service_bindingContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_remote_service_binding.
    def exitAlter_remote_service_binding(self, ctx:TSqlParser.Alter_remote_service_bindingContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_remote_service_binding.
    def enterCreate_remote_service_binding(self, ctx:TSqlParser.Create_remote_service_bindingContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_remote_service_binding.
    def exitCreate_remote_service_binding(self, ctx:TSqlParser.Create_remote_service_bindingContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_resource_pool.
    def enterCreate_resource_pool(self, ctx:TSqlParser.Create_resource_poolContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_resource_pool.
    def exitCreate_resource_pool(self, ctx:TSqlParser.Create_resource_poolContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_resource_governor.
    def enterAlter_resource_governor(self, ctx:TSqlParser.Alter_resource_governorContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_resource_governor.
    def exitAlter_resource_governor(self, ctx:TSqlParser.Alter_resource_governorContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_db_role.
    def enterAlter_db_role(self, ctx:TSqlParser.Alter_db_roleContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_db_role.
    def exitAlter_db_role(self, ctx:TSqlParser.Alter_db_roleContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_db_role.
    def enterCreate_db_role(self, ctx:TSqlParser.Create_db_roleContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_db_role.
    def exitCreate_db_role(self, ctx:TSqlParser.Create_db_roleContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_route.
    def enterCreate_route(self, ctx:TSqlParser.Create_routeContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_route.
    def exitCreate_route(self, ctx:TSqlParser.Create_routeContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_rule.
    def enterCreate_rule(self, ctx:TSqlParser.Create_ruleContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_rule.
    def exitCreate_rule(self, ctx:TSqlParser.Create_ruleContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_schema_sql.
    def enterAlter_schema_sql(self, ctx:TSqlParser.Alter_schema_sqlContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_schema_sql.
    def exitAlter_schema_sql(self, ctx:TSqlParser.Alter_schema_sqlContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_schema.
    def enterCreate_schema(self, ctx:TSqlParser.Create_schemaContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_schema.
    def exitCreate_schema(self, ctx:TSqlParser.Create_schemaContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_schema_azure_sql_dw_and_pdw.
    def enterCreate_schema_azure_sql_dw_and_pdw(self, ctx:TSqlParser.Create_schema_azure_sql_dw_and_pdwContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_schema_azure_sql_dw_and_pdw.
    def exitCreate_schema_azure_sql_dw_and_pdw(self, ctx:TSqlParser.Create_schema_azure_sql_dw_and_pdwContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_schema_azure_sql_dw_and_pdw.
    def enterAlter_schema_azure_sql_dw_and_pdw(self, ctx:TSqlParser.Alter_schema_azure_sql_dw_and_pdwContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_schema_azure_sql_dw_and_pdw.
    def exitAlter_schema_azure_sql_dw_and_pdw(self, ctx:TSqlParser.Alter_schema_azure_sql_dw_and_pdwContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_search_property_list.
    def enterCreate_search_property_list(self, ctx:TSqlParser.Create_search_property_listContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_search_property_list.
    def exitCreate_search_property_list(self, ctx:TSqlParser.Create_search_property_listContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_security_policy.
    def enterCreate_security_policy(self, ctx:TSqlParser.Create_security_policyContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_security_policy.
    def exitCreate_security_policy(self, ctx:TSqlParser.Create_security_policyContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_sequence.
    def enterAlter_sequence(self, ctx:TSqlParser.Alter_sequenceContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_sequence.
    def exitAlter_sequence(self, ctx:TSqlParser.Alter_sequenceContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_sequence.
    def enterCreate_sequence(self, ctx:TSqlParser.Create_sequenceContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_sequence.
    def exitCreate_sequence(self, ctx:TSqlParser.Create_sequenceContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_server_audit.
    def enterAlter_server_audit(self, ctx:TSqlParser.Alter_server_auditContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_server_audit.
    def exitAlter_server_audit(self, ctx:TSqlParser.Alter_server_auditContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_server_audit.
    def enterCreate_server_audit(self, ctx:TSqlParser.Create_server_auditContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_server_audit.
    def exitCreate_server_audit(self, ctx:TSqlParser.Create_server_auditContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_server_audit_specification.
    def enterAlter_server_audit_specification(self, ctx:TSqlParser.Alter_server_audit_specificationContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_server_audit_specification.
    def exitAlter_server_audit_specification(self, ctx:TSqlParser.Alter_server_audit_specificationContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_server_audit_specification.
    def enterCreate_server_audit_specification(self, ctx:TSqlParser.Create_server_audit_specificationContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_server_audit_specification.
    def exitCreate_server_audit_specification(self, ctx:TSqlParser.Create_server_audit_specificationContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_server_configuration.
    def enterAlter_server_configuration(self, ctx:TSqlParser.Alter_server_configurationContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_server_configuration.
    def exitAlter_server_configuration(self, ctx:TSqlParser.Alter_server_configurationContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_server_role.
    def enterAlter_server_role(self, ctx:TSqlParser.Alter_server_roleContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_server_role.
    def exitAlter_server_role(self, ctx:TSqlParser.Alter_server_roleContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_server_role.
    def enterCreate_server_role(self, ctx:TSqlParser.Create_server_roleContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_server_role.
    def exitCreate_server_role(self, ctx:TSqlParser.Create_server_roleContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_server_role_pdw.
    def enterAlter_server_role_pdw(self, ctx:TSqlParser.Alter_server_role_pdwContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_server_role_pdw.
    def exitAlter_server_role_pdw(self, ctx:TSqlParser.Alter_server_role_pdwContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_service.
    def enterAlter_service(self, ctx:TSqlParser.Alter_serviceContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_service.
    def exitAlter_service(self, ctx:TSqlParser.Alter_serviceContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_service.
    def enterCreate_service(self, ctx:TSqlParser.Create_serviceContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_service.
    def exitCreate_service(self, ctx:TSqlParser.Create_serviceContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_service_master_key.
    def enterAlter_service_master_key(self, ctx:TSqlParser.Alter_service_master_keyContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_service_master_key.
    def exitAlter_service_master_key(self, ctx:TSqlParser.Alter_service_master_keyContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_symmetric_key.
    def enterAlter_symmetric_key(self, ctx:TSqlParser.Alter_symmetric_keyContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_symmetric_key.
    def exitAlter_symmetric_key(self, ctx:TSqlParser.Alter_symmetric_keyContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_symmetric_key.
    def enterCreate_symmetric_key(self, ctx:TSqlParser.Create_symmetric_keyContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_symmetric_key.
    def exitCreate_symmetric_key(self, ctx:TSqlParser.Create_symmetric_keyContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_synonym.
    def enterCreate_synonym(self, ctx:TSqlParser.Create_synonymContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_synonym.
    def exitCreate_synonym(self, ctx:TSqlParser.Create_synonymContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_user.
    def enterAlter_user(self, ctx:TSqlParser.Alter_userContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_user.
    def exitAlter_user(self, ctx:TSqlParser.Alter_userContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_user.
    def enterCreate_user(self, ctx:TSqlParser.Create_userContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_user.
    def exitCreate_user(self, ctx:TSqlParser.Create_userContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_user_azure_sql_dw.
    def enterCreate_user_azure_sql_dw(self, ctx:TSqlParser.Create_user_azure_sql_dwContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_user_azure_sql_dw.
    def exitCreate_user_azure_sql_dw(self, ctx:TSqlParser.Create_user_azure_sql_dwContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_user_azure_sql.
    def enterAlter_user_azure_sql(self, ctx:TSqlParser.Alter_user_azure_sqlContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_user_azure_sql.
    def exitAlter_user_azure_sql(self, ctx:TSqlParser.Alter_user_azure_sqlContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_workload_group.
    def enterAlter_workload_group(self, ctx:TSqlParser.Alter_workload_groupContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_workload_group.
    def exitAlter_workload_group(self, ctx:TSqlParser.Alter_workload_groupContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_workload_group.
    def enterCreate_workload_group(self, ctx:TSqlParser.Create_workload_groupContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_workload_group.
    def exitCreate_workload_group(self, ctx:TSqlParser.Create_workload_groupContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_xml_schema_collection.
    def enterCreate_xml_schema_collection(self, ctx:TSqlParser.Create_xml_schema_collectionContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_xml_schema_collection.
    def exitCreate_xml_schema_collection(self, ctx:TSqlParser.Create_xml_schema_collectionContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_queue.
    def enterCreate_queue(self, ctx:TSqlParser.Create_queueContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_queue.
    def exitCreate_queue(self, ctx:TSqlParser.Create_queueContext):
        pass


    # Enter a parse tree produced by TSqlParser#queue_settings.
    def enterQueue_settings(self, ctx:TSqlParser.Queue_settingsContext):
        pass

    # Exit a parse tree produced by TSqlParser#queue_settings.
    def exitQueue_settings(self, ctx:TSqlParser.Queue_settingsContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_queue.
    def enterAlter_queue(self, ctx:TSqlParser.Alter_queueContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_queue.
    def exitAlter_queue(self, ctx:TSqlParser.Alter_queueContext):
        pass


    # Enter a parse tree produced by TSqlParser#queue_action.
    def enterQueue_action(self, ctx:TSqlParser.Queue_actionContext):
        pass

    # Exit a parse tree produced by TSqlParser#queue_action.
    def exitQueue_action(self, ctx:TSqlParser.Queue_actionContext):
        pass


    # Enter a parse tree produced by TSqlParser#queue_rebuild_options.
    def enterQueue_rebuild_options(self, ctx:TSqlParser.Queue_rebuild_optionsContext):
        pass

    # Exit a parse tree produced by TSqlParser#queue_rebuild_options.
    def exitQueue_rebuild_options(self, ctx:TSqlParser.Queue_rebuild_optionsContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_contract.
    def enterCreate_contract(self, ctx:TSqlParser.Create_contractContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_contract.
    def exitCreate_contract(self, ctx:TSqlParser.Create_contractContext):
        pass


    # Enter a parse tree produced by TSqlParser#conversation_statement.
    def enterConversation_statement(self, ctx:TSqlParser.Conversation_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#conversation_statement.
    def exitConversation_statement(self, ctx:TSqlParser.Conversation_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#message_statement.
    def enterMessage_statement(self, ctx:TSqlParser.Message_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#message_statement.
    def exitMessage_statement(self, ctx:TSqlParser.Message_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#merge_statement.
    def enterMerge_statement(self, ctx:TSqlParser.Merge_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#merge_statement.
    def exitMerge_statement(self, ctx:TSqlParser.Merge_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#merge_matched.
    def enterMerge_matched(self, ctx:TSqlParser.Merge_matchedContext):
        pass

    # Exit a parse tree produced by TSqlParser#merge_matched.
    def exitMerge_matched(self, ctx:TSqlParser.Merge_matchedContext):
        pass


    # Enter a parse tree produced by TSqlParser#merge_not_matched.
    def enterMerge_not_matched(self, ctx:TSqlParser.Merge_not_matchedContext):
        pass

    # Exit a parse tree produced by TSqlParser#merge_not_matched.
    def exitMerge_not_matched(self, ctx:TSqlParser.Merge_not_matchedContext):
        pass


    # Enter a parse tree produced by TSqlParser#delete_statement.
    def enterDelete_statement(self, ctx:TSqlParser.Delete_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#delete_statement.
    def exitDelete_statement(self, ctx:TSqlParser.Delete_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#delete_statement_from.
    def enterDelete_statement_from(self, ctx:TSqlParser.Delete_statement_fromContext):
        pass

    # Exit a parse tree produced by TSqlParser#delete_statement_from.
    def exitDelete_statement_from(self, ctx:TSqlParser.Delete_statement_fromContext):
        pass


    # Enter a parse tree produced by TSqlParser#insert_statement.
    def enterInsert_statement(self, ctx:TSqlParser.Insert_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#insert_statement.
    def exitInsert_statement(self, ctx:TSqlParser.Insert_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#insert_statement_value.
    def enterInsert_statement_value(self, ctx:TSqlParser.Insert_statement_valueContext):
        pass

    # Exit a parse tree produced by TSqlParser#insert_statement_value.
    def exitInsert_statement_value(self, ctx:TSqlParser.Insert_statement_valueContext):
        pass


    # Enter a parse tree produced by TSqlParser#receive_statement.
    def enterReceive_statement(self, ctx:TSqlParser.Receive_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#receive_statement.
    def exitReceive_statement(self, ctx:TSqlParser.Receive_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#select_statement.
    def enterSelect_statement(self, ctx:TSqlParser.Select_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#select_statement.
    def exitSelect_statement(self, ctx:TSqlParser.Select_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#time.
    def enterTime(self, ctx:TSqlParser.TimeContext):
        pass

    # Exit a parse tree produced by TSqlParser#time.
    def exitTime(self, ctx:TSqlParser.TimeContext):
        pass


    # Enter a parse tree produced by TSqlParser#update_statement.
    def enterUpdate_statement(self, ctx:TSqlParser.Update_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#update_statement.
    def exitUpdate_statement(self, ctx:TSqlParser.Update_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#output_clause.
    def enterOutput_clause(self, ctx:TSqlParser.Output_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#output_clause.
    def exitOutput_clause(self, ctx:TSqlParser.Output_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#output_dml_list_elem.
    def enterOutput_dml_list_elem(self, ctx:TSqlParser.Output_dml_list_elemContext):
        pass

    # Exit a parse tree produced by TSqlParser#output_dml_list_elem.
    def exitOutput_dml_list_elem(self, ctx:TSqlParser.Output_dml_list_elemContext):
        pass


    # Enter a parse tree produced by TSqlParser#output_column_name.
    def enterOutput_column_name(self, ctx:TSqlParser.Output_column_nameContext):
        pass

    # Exit a parse tree produced by TSqlParser#output_column_name.
    def exitOutput_column_name(self, ctx:TSqlParser.Output_column_nameContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_database.
    def enterCreate_database(self, ctx:TSqlParser.Create_databaseContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_database.
    def exitCreate_database(self, ctx:TSqlParser.Create_databaseContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_index.
    def enterCreate_index(self, ctx:TSqlParser.Create_indexContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_index.
    def exitCreate_index(self, ctx:TSqlParser.Create_indexContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_or_alter_procedure.
    def enterCreate_or_alter_procedure(self, ctx:TSqlParser.Create_or_alter_procedureContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_or_alter_procedure.
    def exitCreate_or_alter_procedure(self, ctx:TSqlParser.Create_or_alter_procedureContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_or_alter_trigger.
    def enterCreate_or_alter_trigger(self, ctx:TSqlParser.Create_or_alter_triggerContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_or_alter_trigger.
    def exitCreate_or_alter_trigger(self, ctx:TSqlParser.Create_or_alter_triggerContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_or_alter_dml_trigger.
    def enterCreate_or_alter_dml_trigger(self, ctx:TSqlParser.Create_or_alter_dml_triggerContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_or_alter_dml_trigger.
    def exitCreate_or_alter_dml_trigger(self, ctx:TSqlParser.Create_or_alter_dml_triggerContext):
        pass


    # Enter a parse tree produced by TSqlParser#dml_trigger_option.
    def enterDml_trigger_option(self, ctx:TSqlParser.Dml_trigger_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#dml_trigger_option.
    def exitDml_trigger_option(self, ctx:TSqlParser.Dml_trigger_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#dml_trigger_operation.
    def enterDml_trigger_operation(self, ctx:TSqlParser.Dml_trigger_operationContext):
        pass

    # Exit a parse tree produced by TSqlParser#dml_trigger_operation.
    def exitDml_trigger_operation(self, ctx:TSqlParser.Dml_trigger_operationContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_or_alter_ddl_trigger.
    def enterCreate_or_alter_ddl_trigger(self, ctx:TSqlParser.Create_or_alter_ddl_triggerContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_or_alter_ddl_trigger.
    def exitCreate_or_alter_ddl_trigger(self, ctx:TSqlParser.Create_or_alter_ddl_triggerContext):
        pass


    # Enter a parse tree produced by TSqlParser#ddl_trigger_operation.
    def enterDdl_trigger_operation(self, ctx:TSqlParser.Ddl_trigger_operationContext):
        pass

    # Exit a parse tree produced by TSqlParser#ddl_trigger_operation.
    def exitDdl_trigger_operation(self, ctx:TSqlParser.Ddl_trigger_operationContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_or_alter_function.
    def enterCreate_or_alter_function(self, ctx:TSqlParser.Create_or_alter_functionContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_or_alter_function.
    def exitCreate_or_alter_function(self, ctx:TSqlParser.Create_or_alter_functionContext):
        pass


    # Enter a parse tree produced by TSqlParser#func_body_returns_select.
    def enterFunc_body_returns_select(self, ctx:TSqlParser.Func_body_returns_selectContext):
        pass

    # Exit a parse tree produced by TSqlParser#func_body_returns_select.
    def exitFunc_body_returns_select(self, ctx:TSqlParser.Func_body_returns_selectContext):
        pass


    # Enter a parse tree produced by TSqlParser#func_body_returns_table.
    def enterFunc_body_returns_table(self, ctx:TSqlParser.Func_body_returns_tableContext):
        pass

    # Exit a parse tree produced by TSqlParser#func_body_returns_table.
    def exitFunc_body_returns_table(self, ctx:TSqlParser.Func_body_returns_tableContext):
        pass


    # Enter a parse tree produced by TSqlParser#func_body_returns_scalar.
    def enterFunc_body_returns_scalar(self, ctx:TSqlParser.Func_body_returns_scalarContext):
        pass

    # Exit a parse tree produced by TSqlParser#func_body_returns_scalar.
    def exitFunc_body_returns_scalar(self, ctx:TSqlParser.Func_body_returns_scalarContext):
        pass


    # Enter a parse tree produced by TSqlParser#procedure_param.
    def enterProcedure_param(self, ctx:TSqlParser.Procedure_paramContext):
        pass

    # Exit a parse tree produced by TSqlParser#procedure_param.
    def exitProcedure_param(self, ctx:TSqlParser.Procedure_paramContext):
        pass


    # Enter a parse tree produced by TSqlParser#procedure_option.
    def enterProcedure_option(self, ctx:TSqlParser.Procedure_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#procedure_option.
    def exitProcedure_option(self, ctx:TSqlParser.Procedure_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#function_option.
    def enterFunction_option(self, ctx:TSqlParser.Function_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#function_option.
    def exitFunction_option(self, ctx:TSqlParser.Function_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_statistics.
    def enterCreate_statistics(self, ctx:TSqlParser.Create_statisticsContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_statistics.
    def exitCreate_statistics(self, ctx:TSqlParser.Create_statisticsContext):
        pass


    # Enter a parse tree produced by TSqlParser#update_statistics.
    def enterUpdate_statistics(self, ctx:TSqlParser.Update_statisticsContext):
        pass

    # Exit a parse tree produced by TSqlParser#update_statistics.
    def exitUpdate_statistics(self, ctx:TSqlParser.Update_statisticsContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_table.
    def enterCreate_table(self, ctx:TSqlParser.Create_tableContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_table.
    def exitCreate_table(self, ctx:TSqlParser.Create_tableContext):
        pass


    # Enter a parse tree produced by TSqlParser#table_options.
    def enterTable_options(self, ctx:TSqlParser.Table_optionsContext):
        pass

    # Exit a parse tree produced by TSqlParser#table_options.
    def exitTable_options(self, ctx:TSqlParser.Table_optionsContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_view.
    def enterCreate_view(self, ctx:TSqlParser.Create_viewContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_view.
    def exitCreate_view(self, ctx:TSqlParser.Create_viewContext):
        pass


    # Enter a parse tree produced by TSqlParser#view_attribute.
    def enterView_attribute(self, ctx:TSqlParser.View_attributeContext):
        pass

    # Exit a parse tree produced by TSqlParser#view_attribute.
    def exitView_attribute(self, ctx:TSqlParser.View_attributeContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_table.
    def enterAlter_table(self, ctx:TSqlParser.Alter_tableContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_table.
    def exitAlter_table(self, ctx:TSqlParser.Alter_tableContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_database.
    def enterAlter_database(self, ctx:TSqlParser.Alter_databaseContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_database.
    def exitAlter_database(self, ctx:TSqlParser.Alter_databaseContext):
        pass


    # Enter a parse tree produced by TSqlParser#database_optionspec.
    def enterDatabase_optionspec(self, ctx:TSqlParser.Database_optionspecContext):
        pass

    # Exit a parse tree produced by TSqlParser#database_optionspec.
    def exitDatabase_optionspec(self, ctx:TSqlParser.Database_optionspecContext):
        pass


    # Enter a parse tree produced by TSqlParser#auto_option.
    def enterAuto_option(self, ctx:TSqlParser.Auto_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#auto_option.
    def exitAuto_option(self, ctx:TSqlParser.Auto_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#change_tracking_option.
    def enterChange_tracking_option(self, ctx:TSqlParser.Change_tracking_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#change_tracking_option.
    def exitChange_tracking_option(self, ctx:TSqlParser.Change_tracking_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#change_tracking_option_list.
    def enterChange_tracking_option_list(self, ctx:TSqlParser.Change_tracking_option_listContext):
        pass

    # Exit a parse tree produced by TSqlParser#change_tracking_option_list.
    def exitChange_tracking_option_list(self, ctx:TSqlParser.Change_tracking_option_listContext):
        pass


    # Enter a parse tree produced by TSqlParser#containment_option.
    def enterContainment_option(self, ctx:TSqlParser.Containment_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#containment_option.
    def exitContainment_option(self, ctx:TSqlParser.Containment_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#cursor_option.
    def enterCursor_option(self, ctx:TSqlParser.Cursor_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#cursor_option.
    def exitCursor_option(self, ctx:TSqlParser.Cursor_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#alter_endpoint.
    def enterAlter_endpoint(self, ctx:TSqlParser.Alter_endpointContext):
        pass

    # Exit a parse tree produced by TSqlParser#alter_endpoint.
    def exitAlter_endpoint(self, ctx:TSqlParser.Alter_endpointContext):
        pass


    # Enter a parse tree produced by TSqlParser#database_mirroring_option.
    def enterDatabase_mirroring_option(self, ctx:TSqlParser.Database_mirroring_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#database_mirroring_option.
    def exitDatabase_mirroring_option(self, ctx:TSqlParser.Database_mirroring_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#mirroring_set_option.
    def enterMirroring_set_option(self, ctx:TSqlParser.Mirroring_set_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#mirroring_set_option.
    def exitMirroring_set_option(self, ctx:TSqlParser.Mirroring_set_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#mirroring_partner.
    def enterMirroring_partner(self, ctx:TSqlParser.Mirroring_partnerContext):
        pass

    # Exit a parse tree produced by TSqlParser#mirroring_partner.
    def exitMirroring_partner(self, ctx:TSqlParser.Mirroring_partnerContext):
        pass


    # Enter a parse tree produced by TSqlParser#mirroring_witness.
    def enterMirroring_witness(self, ctx:TSqlParser.Mirroring_witnessContext):
        pass

    # Exit a parse tree produced by TSqlParser#mirroring_witness.
    def exitMirroring_witness(self, ctx:TSqlParser.Mirroring_witnessContext):
        pass


    # Enter a parse tree produced by TSqlParser#witness_partner_equal.
    def enterWitness_partner_equal(self, ctx:TSqlParser.Witness_partner_equalContext):
        pass

    # Exit a parse tree produced by TSqlParser#witness_partner_equal.
    def exitWitness_partner_equal(self, ctx:TSqlParser.Witness_partner_equalContext):
        pass


    # Enter a parse tree produced by TSqlParser#partner_option.
    def enterPartner_option(self, ctx:TSqlParser.Partner_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#partner_option.
    def exitPartner_option(self, ctx:TSqlParser.Partner_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#witness_option.
    def enterWitness_option(self, ctx:TSqlParser.Witness_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#witness_option.
    def exitWitness_option(self, ctx:TSqlParser.Witness_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#witness_server.
    def enterWitness_server(self, ctx:TSqlParser.Witness_serverContext):
        pass

    # Exit a parse tree produced by TSqlParser#witness_server.
    def exitWitness_server(self, ctx:TSqlParser.Witness_serverContext):
        pass


    # Enter a parse tree produced by TSqlParser#partner_server.
    def enterPartner_server(self, ctx:TSqlParser.Partner_serverContext):
        pass

    # Exit a parse tree produced by TSqlParser#partner_server.
    def exitPartner_server(self, ctx:TSqlParser.Partner_serverContext):
        pass


    # Enter a parse tree produced by TSqlParser#mirroring_host_port_seperator.
    def enterMirroring_host_port_seperator(self, ctx:TSqlParser.Mirroring_host_port_seperatorContext):
        pass

    # Exit a parse tree produced by TSqlParser#mirroring_host_port_seperator.
    def exitMirroring_host_port_seperator(self, ctx:TSqlParser.Mirroring_host_port_seperatorContext):
        pass


    # Enter a parse tree produced by TSqlParser#partner_server_tcp_prefix.
    def enterPartner_server_tcp_prefix(self, ctx:TSqlParser.Partner_server_tcp_prefixContext):
        pass

    # Exit a parse tree produced by TSqlParser#partner_server_tcp_prefix.
    def exitPartner_server_tcp_prefix(self, ctx:TSqlParser.Partner_server_tcp_prefixContext):
        pass


    # Enter a parse tree produced by TSqlParser#port_number.
    def enterPort_number(self, ctx:TSqlParser.Port_numberContext):
        pass

    # Exit a parse tree produced by TSqlParser#port_number.
    def exitPort_number(self, ctx:TSqlParser.Port_numberContext):
        pass


    # Enter a parse tree produced by TSqlParser#host.
    def enterHost(self, ctx:TSqlParser.HostContext):
        pass

    # Exit a parse tree produced by TSqlParser#host.
    def exitHost(self, ctx:TSqlParser.HostContext):
        pass


    # Enter a parse tree produced by TSqlParser#date_correlation_optimization_option.
    def enterDate_correlation_optimization_option(self, ctx:TSqlParser.Date_correlation_optimization_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#date_correlation_optimization_option.
    def exitDate_correlation_optimization_option(self, ctx:TSqlParser.Date_correlation_optimization_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#db_encryption_option.
    def enterDb_encryption_option(self, ctx:TSqlParser.Db_encryption_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#db_encryption_option.
    def exitDb_encryption_option(self, ctx:TSqlParser.Db_encryption_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#db_state_option.
    def enterDb_state_option(self, ctx:TSqlParser.Db_state_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#db_state_option.
    def exitDb_state_option(self, ctx:TSqlParser.Db_state_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#db_update_option.
    def enterDb_update_option(self, ctx:TSqlParser.Db_update_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#db_update_option.
    def exitDb_update_option(self, ctx:TSqlParser.Db_update_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#db_user_access_option.
    def enterDb_user_access_option(self, ctx:TSqlParser.Db_user_access_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#db_user_access_option.
    def exitDb_user_access_option(self, ctx:TSqlParser.Db_user_access_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#delayed_durability_option.
    def enterDelayed_durability_option(self, ctx:TSqlParser.Delayed_durability_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#delayed_durability_option.
    def exitDelayed_durability_option(self, ctx:TSqlParser.Delayed_durability_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#external_access_option.
    def enterExternal_access_option(self, ctx:TSqlParser.External_access_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#external_access_option.
    def exitExternal_access_option(self, ctx:TSqlParser.External_access_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#hadr_options.
    def enterHadr_options(self, ctx:TSqlParser.Hadr_optionsContext):
        pass

    # Exit a parse tree produced by TSqlParser#hadr_options.
    def exitHadr_options(self, ctx:TSqlParser.Hadr_optionsContext):
        pass


    # Enter a parse tree produced by TSqlParser#mixed_page_allocation_option.
    def enterMixed_page_allocation_option(self, ctx:TSqlParser.Mixed_page_allocation_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#mixed_page_allocation_option.
    def exitMixed_page_allocation_option(self, ctx:TSqlParser.Mixed_page_allocation_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#parameterization_option.
    def enterParameterization_option(self, ctx:TSqlParser.Parameterization_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#parameterization_option.
    def exitParameterization_option(self, ctx:TSqlParser.Parameterization_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#recovery_option.
    def enterRecovery_option(self, ctx:TSqlParser.Recovery_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#recovery_option.
    def exitRecovery_option(self, ctx:TSqlParser.Recovery_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#service_broker_option.
    def enterService_broker_option(self, ctx:TSqlParser.Service_broker_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#service_broker_option.
    def exitService_broker_option(self, ctx:TSqlParser.Service_broker_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#snapshot_option.
    def enterSnapshot_option(self, ctx:TSqlParser.Snapshot_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#snapshot_option.
    def exitSnapshot_option(self, ctx:TSqlParser.Snapshot_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#sql_option.
    def enterSql_option(self, ctx:TSqlParser.Sql_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#sql_option.
    def exitSql_option(self, ctx:TSqlParser.Sql_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#target_recovery_time_option.
    def enterTarget_recovery_time_option(self, ctx:TSqlParser.Target_recovery_time_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#target_recovery_time_option.
    def exitTarget_recovery_time_option(self, ctx:TSqlParser.Target_recovery_time_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#termination.
    def enterTermination(self, ctx:TSqlParser.TerminationContext):
        pass

    # Exit a parse tree produced by TSqlParser#termination.
    def exitTermination(self, ctx:TSqlParser.TerminationContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_index.
    def enterDrop_index(self, ctx:TSqlParser.Drop_indexContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_index.
    def exitDrop_index(self, ctx:TSqlParser.Drop_indexContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_relational_or_xml_or_spatial_index.
    def enterDrop_relational_or_xml_or_spatial_index(self, ctx:TSqlParser.Drop_relational_or_xml_or_spatial_indexContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_relational_or_xml_or_spatial_index.
    def exitDrop_relational_or_xml_or_spatial_index(self, ctx:TSqlParser.Drop_relational_or_xml_or_spatial_indexContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_backward_compatible_index.
    def enterDrop_backward_compatible_index(self, ctx:TSqlParser.Drop_backward_compatible_indexContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_backward_compatible_index.
    def exitDrop_backward_compatible_index(self, ctx:TSqlParser.Drop_backward_compatible_indexContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_procedure.
    def enterDrop_procedure(self, ctx:TSqlParser.Drop_procedureContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_procedure.
    def exitDrop_procedure(self, ctx:TSqlParser.Drop_procedureContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_trigger.
    def enterDrop_trigger(self, ctx:TSqlParser.Drop_triggerContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_trigger.
    def exitDrop_trigger(self, ctx:TSqlParser.Drop_triggerContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_dml_trigger.
    def enterDrop_dml_trigger(self, ctx:TSqlParser.Drop_dml_triggerContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_dml_trigger.
    def exitDrop_dml_trigger(self, ctx:TSqlParser.Drop_dml_triggerContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_ddl_trigger.
    def enterDrop_ddl_trigger(self, ctx:TSqlParser.Drop_ddl_triggerContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_ddl_trigger.
    def exitDrop_ddl_trigger(self, ctx:TSqlParser.Drop_ddl_triggerContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_function.
    def enterDrop_function(self, ctx:TSqlParser.Drop_functionContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_function.
    def exitDrop_function(self, ctx:TSqlParser.Drop_functionContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_statistics.
    def enterDrop_statistics(self, ctx:TSqlParser.Drop_statisticsContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_statistics.
    def exitDrop_statistics(self, ctx:TSqlParser.Drop_statisticsContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_table.
    def enterDrop_table(self, ctx:TSqlParser.Drop_tableContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_table.
    def exitDrop_table(self, ctx:TSqlParser.Drop_tableContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_view.
    def enterDrop_view(self, ctx:TSqlParser.Drop_viewContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_view.
    def exitDrop_view(self, ctx:TSqlParser.Drop_viewContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_type.
    def enterCreate_type(self, ctx:TSqlParser.Create_typeContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_type.
    def exitCreate_type(self, ctx:TSqlParser.Create_typeContext):
        pass


    # Enter a parse tree produced by TSqlParser#drop_type.
    def enterDrop_type(self, ctx:TSqlParser.Drop_typeContext):
        pass

    # Exit a parse tree produced by TSqlParser#drop_type.
    def exitDrop_type(self, ctx:TSqlParser.Drop_typeContext):
        pass


    # Enter a parse tree produced by TSqlParser#rowset_function_limited.
    def enterRowset_function_limited(self, ctx:TSqlParser.Rowset_function_limitedContext):
        pass

    # Exit a parse tree produced by TSqlParser#rowset_function_limited.
    def exitRowset_function_limited(self, ctx:TSqlParser.Rowset_function_limitedContext):
        pass


    # Enter a parse tree produced by TSqlParser#openquery.
    def enterOpenquery(self, ctx:TSqlParser.OpenqueryContext):
        pass

    # Exit a parse tree produced by TSqlParser#openquery.
    def exitOpenquery(self, ctx:TSqlParser.OpenqueryContext):
        pass


    # Enter a parse tree produced by TSqlParser#opendatasource.
    def enterOpendatasource(self, ctx:TSqlParser.OpendatasourceContext):
        pass

    # Exit a parse tree produced by TSqlParser#opendatasource.
    def exitOpendatasource(self, ctx:TSqlParser.OpendatasourceContext):
        pass


    # Enter a parse tree produced by TSqlParser#declare_statement.
    def enterDeclare_statement(self, ctx:TSqlParser.Declare_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#declare_statement.
    def exitDeclare_statement(self, ctx:TSqlParser.Declare_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#cursor_statement.
    def enterCursor_statement(self, ctx:TSqlParser.Cursor_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#cursor_statement.
    def exitCursor_statement(self, ctx:TSqlParser.Cursor_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#backup_database.
    def enterBackup_database(self, ctx:TSqlParser.Backup_databaseContext):
        pass

    # Exit a parse tree produced by TSqlParser#backup_database.
    def exitBackup_database(self, ctx:TSqlParser.Backup_databaseContext):
        pass


    # Enter a parse tree produced by TSqlParser#backup_log.
    def enterBackup_log(self, ctx:TSqlParser.Backup_logContext):
        pass

    # Exit a parse tree produced by TSqlParser#backup_log.
    def exitBackup_log(self, ctx:TSqlParser.Backup_logContext):
        pass


    # Enter a parse tree produced by TSqlParser#backup_certificate.
    def enterBackup_certificate(self, ctx:TSqlParser.Backup_certificateContext):
        pass

    # Exit a parse tree produced by TSqlParser#backup_certificate.
    def exitBackup_certificate(self, ctx:TSqlParser.Backup_certificateContext):
        pass


    # Enter a parse tree produced by TSqlParser#backup_master_key.
    def enterBackup_master_key(self, ctx:TSqlParser.Backup_master_keyContext):
        pass

    # Exit a parse tree produced by TSqlParser#backup_master_key.
    def exitBackup_master_key(self, ctx:TSqlParser.Backup_master_keyContext):
        pass


    # Enter a parse tree produced by TSqlParser#backup_service_master_key.
    def enterBackup_service_master_key(self, ctx:TSqlParser.Backup_service_master_keyContext):
        pass

    # Exit a parse tree produced by TSqlParser#backup_service_master_key.
    def exitBackup_service_master_key(self, ctx:TSqlParser.Backup_service_master_keyContext):
        pass


    # Enter a parse tree produced by TSqlParser#execute_statement.
    def enterExecute_statement(self, ctx:TSqlParser.Execute_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#execute_statement.
    def exitExecute_statement(self, ctx:TSqlParser.Execute_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#execute_body.
    def enterExecute_body(self, ctx:TSqlParser.Execute_bodyContext):
        pass

    # Exit a parse tree produced by TSqlParser#execute_body.
    def exitExecute_body(self, ctx:TSqlParser.Execute_bodyContext):
        pass


    # Enter a parse tree produced by TSqlParser#execute_statement_arg.
    def enterExecute_statement_arg(self, ctx:TSqlParser.Execute_statement_argContext):
        pass

    # Exit a parse tree produced by TSqlParser#execute_statement_arg.
    def exitExecute_statement_arg(self, ctx:TSqlParser.Execute_statement_argContext):
        pass


    # Enter a parse tree produced by TSqlParser#execute_var_string.
    def enterExecute_var_string(self, ctx:TSqlParser.Execute_var_stringContext):
        pass

    # Exit a parse tree produced by TSqlParser#execute_var_string.
    def exitExecute_var_string(self, ctx:TSqlParser.Execute_var_stringContext):
        pass


    # Enter a parse tree produced by TSqlParser#security_statement.
    def enterSecurity_statement(self, ctx:TSqlParser.Security_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#security_statement.
    def exitSecurity_statement(self, ctx:TSqlParser.Security_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_certificate.
    def enterCreate_certificate(self, ctx:TSqlParser.Create_certificateContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_certificate.
    def exitCreate_certificate(self, ctx:TSqlParser.Create_certificateContext):
        pass


    # Enter a parse tree produced by TSqlParser#existing_keys.
    def enterExisting_keys(self, ctx:TSqlParser.Existing_keysContext):
        pass

    # Exit a parse tree produced by TSqlParser#existing_keys.
    def exitExisting_keys(self, ctx:TSqlParser.Existing_keysContext):
        pass


    # Enter a parse tree produced by TSqlParser#private_key_options.
    def enterPrivate_key_options(self, ctx:TSqlParser.Private_key_optionsContext):
        pass

    # Exit a parse tree produced by TSqlParser#private_key_options.
    def exitPrivate_key_options(self, ctx:TSqlParser.Private_key_optionsContext):
        pass


    # Enter a parse tree produced by TSqlParser#generate_new_keys.
    def enterGenerate_new_keys(self, ctx:TSqlParser.Generate_new_keysContext):
        pass

    # Exit a parse tree produced by TSqlParser#generate_new_keys.
    def exitGenerate_new_keys(self, ctx:TSqlParser.Generate_new_keysContext):
        pass


    # Enter a parse tree produced by TSqlParser#date_options.
    def enterDate_options(self, ctx:TSqlParser.Date_optionsContext):
        pass

    # Exit a parse tree produced by TSqlParser#date_options.
    def exitDate_options(self, ctx:TSqlParser.Date_optionsContext):
        pass


    # Enter a parse tree produced by TSqlParser#open_key.
    def enterOpen_key(self, ctx:TSqlParser.Open_keyContext):
        pass

    # Exit a parse tree produced by TSqlParser#open_key.
    def exitOpen_key(self, ctx:TSqlParser.Open_keyContext):
        pass


    # Enter a parse tree produced by TSqlParser#close_key.
    def enterClose_key(self, ctx:TSqlParser.Close_keyContext):
        pass

    # Exit a parse tree produced by TSqlParser#close_key.
    def exitClose_key(self, ctx:TSqlParser.Close_keyContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_key.
    def enterCreate_key(self, ctx:TSqlParser.Create_keyContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_key.
    def exitCreate_key(self, ctx:TSqlParser.Create_keyContext):
        pass


    # Enter a parse tree produced by TSqlParser#key_options.
    def enterKey_options(self, ctx:TSqlParser.Key_optionsContext):
        pass

    # Exit a parse tree produced by TSqlParser#key_options.
    def exitKey_options(self, ctx:TSqlParser.Key_optionsContext):
        pass


    # Enter a parse tree produced by TSqlParser#algorithm.
    def enterAlgorithm(self, ctx:TSqlParser.AlgorithmContext):
        pass

    # Exit a parse tree produced by TSqlParser#algorithm.
    def exitAlgorithm(self, ctx:TSqlParser.AlgorithmContext):
        pass


    # Enter a parse tree produced by TSqlParser#encryption_mechanism.
    def enterEncryption_mechanism(self, ctx:TSqlParser.Encryption_mechanismContext):
        pass

    # Exit a parse tree produced by TSqlParser#encryption_mechanism.
    def exitEncryption_mechanism(self, ctx:TSqlParser.Encryption_mechanismContext):
        pass


    # Enter a parse tree produced by TSqlParser#decryption_mechanism.
    def enterDecryption_mechanism(self, ctx:TSqlParser.Decryption_mechanismContext):
        pass

    # Exit a parse tree produced by TSqlParser#decryption_mechanism.
    def exitDecryption_mechanism(self, ctx:TSqlParser.Decryption_mechanismContext):
        pass


    # Enter a parse tree produced by TSqlParser#grant_permission.
    def enterGrant_permission(self, ctx:TSqlParser.Grant_permissionContext):
        pass

    # Exit a parse tree produced by TSqlParser#grant_permission.
    def exitGrant_permission(self, ctx:TSqlParser.Grant_permissionContext):
        pass


    # Enter a parse tree produced by TSqlParser#set_statement.
    def enterSet_statement(self, ctx:TSqlParser.Set_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#set_statement.
    def exitSet_statement(self, ctx:TSqlParser.Set_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#transaction_statement.
    def enterTransaction_statement(self, ctx:TSqlParser.Transaction_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#transaction_statement.
    def exitTransaction_statement(self, ctx:TSqlParser.Transaction_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#go_statement.
    def enterGo_statement(self, ctx:TSqlParser.Go_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#go_statement.
    def exitGo_statement(self, ctx:TSqlParser.Go_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#use_statement.
    def enterUse_statement(self, ctx:TSqlParser.Use_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#use_statement.
    def exitUse_statement(self, ctx:TSqlParser.Use_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#setuser_statement.
    def enterSetuser_statement(self, ctx:TSqlParser.Setuser_statementContext):
        pass

    # Exit a parse tree produced by TSqlParser#setuser_statement.
    def exitSetuser_statement(self, ctx:TSqlParser.Setuser_statementContext):
        pass


    # Enter a parse tree produced by TSqlParser#dbcc_clause.
    def enterDbcc_clause(self, ctx:TSqlParser.Dbcc_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#dbcc_clause.
    def exitDbcc_clause(self, ctx:TSqlParser.Dbcc_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#dbcc_options.
    def enterDbcc_options(self, ctx:TSqlParser.Dbcc_optionsContext):
        pass

    # Exit a parse tree produced by TSqlParser#dbcc_options.
    def exitDbcc_options(self, ctx:TSqlParser.Dbcc_optionsContext):
        pass


    # Enter a parse tree produced by TSqlParser#execute_clause.
    def enterExecute_clause(self, ctx:TSqlParser.Execute_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#execute_clause.
    def exitExecute_clause(self, ctx:TSqlParser.Execute_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#declare_local.
    def enterDeclare_local(self, ctx:TSqlParser.Declare_localContext):
        pass

    # Exit a parse tree produced by TSqlParser#declare_local.
    def exitDeclare_local(self, ctx:TSqlParser.Declare_localContext):
        pass


    # Enter a parse tree produced by TSqlParser#table_type_definition.
    def enterTable_type_definition(self, ctx:TSqlParser.Table_type_definitionContext):
        pass

    # Exit a parse tree produced by TSqlParser#table_type_definition.
    def exitTable_type_definition(self, ctx:TSqlParser.Table_type_definitionContext):
        pass


    # Enter a parse tree produced by TSqlParser#xml_type_definition.
    def enterXml_type_definition(self, ctx:TSqlParser.Xml_type_definitionContext):
        pass

    # Exit a parse tree produced by TSqlParser#xml_type_definition.
    def exitXml_type_definition(self, ctx:TSqlParser.Xml_type_definitionContext):
        pass


    # Enter a parse tree produced by TSqlParser#xml_schema_collection.
    def enterXml_schema_collection(self, ctx:TSqlParser.Xml_schema_collectionContext):
        pass

    # Exit a parse tree produced by TSqlParser#xml_schema_collection.
    def exitXml_schema_collection(self, ctx:TSqlParser.Xml_schema_collectionContext):
        pass


    # Enter a parse tree produced by TSqlParser#column_def_table_constraints.
    def enterColumn_def_table_constraints(self, ctx:TSqlParser.Column_def_table_constraintsContext):
        pass

    # Exit a parse tree produced by TSqlParser#column_def_table_constraints.
    def exitColumn_def_table_constraints(self, ctx:TSqlParser.Column_def_table_constraintsContext):
        pass


    # Enter a parse tree produced by TSqlParser#column_def_table_constraint.
    def enterColumn_def_table_constraint(self, ctx:TSqlParser.Column_def_table_constraintContext):
        pass

    # Exit a parse tree produced by TSqlParser#column_def_table_constraint.
    def exitColumn_def_table_constraint(self, ctx:TSqlParser.Column_def_table_constraintContext):
        pass


    # Enter a parse tree produced by TSqlParser#column_definition.
    def enterColumn_definition(self, ctx:TSqlParser.Column_definitionContext):
        pass

    # Exit a parse tree produced by TSqlParser#column_definition.
    def exitColumn_definition(self, ctx:TSqlParser.Column_definitionContext):
        pass


    # Enter a parse tree produced by TSqlParser#materialized_column_definition.
    def enterMaterialized_column_definition(self, ctx:TSqlParser.Materialized_column_definitionContext):
        pass

    # Exit a parse tree produced by TSqlParser#materialized_column_definition.
    def exitMaterialized_column_definition(self, ctx:TSqlParser.Materialized_column_definitionContext):
        pass


    # Enter a parse tree produced by TSqlParser#column_constraint.
    def enterColumn_constraint(self, ctx:TSqlParser.Column_constraintContext):
        pass

    # Exit a parse tree produced by TSqlParser#column_constraint.
    def exitColumn_constraint(self, ctx:TSqlParser.Column_constraintContext):
        pass


    # Enter a parse tree produced by TSqlParser#table_constraint.
    def enterTable_constraint(self, ctx:TSqlParser.Table_constraintContext):
        pass

    # Exit a parse tree produced by TSqlParser#table_constraint.
    def exitTable_constraint(self, ctx:TSqlParser.Table_constraintContext):
        pass


    # Enter a parse tree produced by TSqlParser#on_delete.
    def enterOn_delete(self, ctx:TSqlParser.On_deleteContext):
        pass

    # Exit a parse tree produced by TSqlParser#on_delete.
    def exitOn_delete(self, ctx:TSqlParser.On_deleteContext):
        pass


    # Enter a parse tree produced by TSqlParser#on_update.
    def enterOn_update(self, ctx:TSqlParser.On_updateContext):
        pass

    # Exit a parse tree produced by TSqlParser#on_update.
    def exitOn_update(self, ctx:TSqlParser.On_updateContext):
        pass


    # Enter a parse tree produced by TSqlParser#index_options.
    def enterIndex_options(self, ctx:TSqlParser.Index_optionsContext):
        pass

    # Exit a parse tree produced by TSqlParser#index_options.
    def exitIndex_options(self, ctx:TSqlParser.Index_optionsContext):
        pass


    # Enter a parse tree produced by TSqlParser#index_option.
    def enterIndex_option(self, ctx:TSqlParser.Index_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#index_option.
    def exitIndex_option(self, ctx:TSqlParser.Index_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#declare_cursor.
    def enterDeclare_cursor(self, ctx:TSqlParser.Declare_cursorContext):
        pass

    # Exit a parse tree produced by TSqlParser#declare_cursor.
    def exitDeclare_cursor(self, ctx:TSqlParser.Declare_cursorContext):
        pass


    # Enter a parse tree produced by TSqlParser#declare_set_cursor_common.
    def enterDeclare_set_cursor_common(self, ctx:TSqlParser.Declare_set_cursor_commonContext):
        pass

    # Exit a parse tree produced by TSqlParser#declare_set_cursor_common.
    def exitDeclare_set_cursor_common(self, ctx:TSqlParser.Declare_set_cursor_commonContext):
        pass


    # Enter a parse tree produced by TSqlParser#declare_set_cursor_common_partial.
    def enterDeclare_set_cursor_common_partial(self, ctx:TSqlParser.Declare_set_cursor_common_partialContext):
        pass

    # Exit a parse tree produced by TSqlParser#declare_set_cursor_common_partial.
    def exitDeclare_set_cursor_common_partial(self, ctx:TSqlParser.Declare_set_cursor_common_partialContext):
        pass


    # Enter a parse tree produced by TSqlParser#fetch_cursor.
    def enterFetch_cursor(self, ctx:TSqlParser.Fetch_cursorContext):
        pass

    # Exit a parse tree produced by TSqlParser#fetch_cursor.
    def exitFetch_cursor(self, ctx:TSqlParser.Fetch_cursorContext):
        pass


    # Enter a parse tree produced by TSqlParser#set_special.
    def enterSet_special(self, ctx:TSqlParser.Set_specialContext):
        pass

    # Exit a parse tree produced by TSqlParser#set_special.
    def exitSet_special(self, ctx:TSqlParser.Set_specialContext):
        pass


    # Enter a parse tree produced by TSqlParser#constant_LOCAL_ID.
    def enterConstant_LOCAL_ID(self, ctx:TSqlParser.Constant_LOCAL_IDContext):
        pass

    # Exit a parse tree produced by TSqlParser#constant_LOCAL_ID.
    def exitConstant_LOCAL_ID(self, ctx:TSqlParser.Constant_LOCAL_IDContext):
        pass


    # Enter a parse tree produced by TSqlParser#expression.
    def enterExpression(self, ctx:TSqlParser.ExpressionContext):
        pass

    # Exit a parse tree produced by TSqlParser#expression.
    def exitExpression(self, ctx:TSqlParser.ExpressionContext):
        pass


    # Enter a parse tree produced by TSqlParser#primitive_expression.
    def enterPrimitive_expression(self, ctx:TSqlParser.Primitive_expressionContext):
        pass

    # Exit a parse tree produced by TSqlParser#primitive_expression.
    def exitPrimitive_expression(self, ctx:TSqlParser.Primitive_expressionContext):
        pass


    # Enter a parse tree produced by TSqlParser#case_expression.
    def enterCase_expression(self, ctx:TSqlParser.Case_expressionContext):
        pass

    # Exit a parse tree produced by TSqlParser#case_expression.
    def exitCase_expression(self, ctx:TSqlParser.Case_expressionContext):
        pass


    # Enter a parse tree produced by TSqlParser#unary_operator_expression.
    def enterUnary_operator_expression(self, ctx:TSqlParser.Unary_operator_expressionContext):
        pass

    # Exit a parse tree produced by TSqlParser#unary_operator_expression.
    def exitUnary_operator_expression(self, ctx:TSqlParser.Unary_operator_expressionContext):
        pass


    # Enter a parse tree produced by TSqlParser#bracket_expression.
    def enterBracket_expression(self, ctx:TSqlParser.Bracket_expressionContext):
        pass

    # Exit a parse tree produced by TSqlParser#bracket_expression.
    def exitBracket_expression(self, ctx:TSqlParser.Bracket_expressionContext):
        pass


    # Enter a parse tree produced by TSqlParser#constant_expression.
    def enterConstant_expression(self, ctx:TSqlParser.Constant_expressionContext):
        pass

    # Exit a parse tree produced by TSqlParser#constant_expression.
    def exitConstant_expression(self, ctx:TSqlParser.Constant_expressionContext):
        pass


    # Enter a parse tree produced by TSqlParser#subquery.
    def enterSubquery(self, ctx:TSqlParser.SubqueryContext):
        pass

    # Exit a parse tree produced by TSqlParser#subquery.
    def exitSubquery(self, ctx:TSqlParser.SubqueryContext):
        pass


    # Enter a parse tree produced by TSqlParser#with_expression.
    def enterWith_expression(self, ctx:TSqlParser.With_expressionContext):
        pass

    # Exit a parse tree produced by TSqlParser#with_expression.
    def exitWith_expression(self, ctx:TSqlParser.With_expressionContext):
        pass


    # Enter a parse tree produced by TSqlParser#common_table_expression.
    def enterCommon_table_expression(self, ctx:TSqlParser.Common_table_expressionContext):
        pass

    # Exit a parse tree produced by TSqlParser#common_table_expression.
    def exitCommon_table_expression(self, ctx:TSqlParser.Common_table_expressionContext):
        pass


    # Enter a parse tree produced by TSqlParser#update_elem.
    def enterUpdate_elem(self, ctx:TSqlParser.Update_elemContext):
        pass

    # Exit a parse tree produced by TSqlParser#update_elem.
    def exitUpdate_elem(self, ctx:TSqlParser.Update_elemContext):
        pass


    # Enter a parse tree produced by TSqlParser#search_condition_list.
    def enterSearch_condition_list(self, ctx:TSqlParser.Search_condition_listContext):
        pass

    # Exit a parse tree produced by TSqlParser#search_condition_list.
    def exitSearch_condition_list(self, ctx:TSqlParser.Search_condition_listContext):
        pass


    # Enter a parse tree produced by TSqlParser#search_condition.
    def enterSearch_condition(self, ctx:TSqlParser.Search_conditionContext):
        pass

    # Exit a parse tree produced by TSqlParser#search_condition.
    def exitSearch_condition(self, ctx:TSqlParser.Search_conditionContext):
        pass


    # Enter a parse tree produced by TSqlParser#search_condition_and.
    def enterSearch_condition_and(self, ctx:TSqlParser.Search_condition_andContext):
        pass

    # Exit a parse tree produced by TSqlParser#search_condition_and.
    def exitSearch_condition_and(self, ctx:TSqlParser.Search_condition_andContext):
        pass


    # Enter a parse tree produced by TSqlParser#search_condition_not.
    def enterSearch_condition_not(self, ctx:TSqlParser.Search_condition_notContext):
        pass

    # Exit a parse tree produced by TSqlParser#search_condition_not.
    def exitSearch_condition_not(self, ctx:TSqlParser.Search_condition_notContext):
        pass


    # Enter a parse tree produced by TSqlParser#predicate.
    def enterPredicate(self, ctx:TSqlParser.PredicateContext):
        pass

    # Exit a parse tree produced by TSqlParser#predicate.
    def exitPredicate(self, ctx:TSqlParser.PredicateContext):
        pass


    # Enter a parse tree produced by TSqlParser#query_expression.
    def enterQuery_expression(self, ctx:TSqlParser.Query_expressionContext):
        pass

    # Exit a parse tree produced by TSqlParser#query_expression.
    def exitQuery_expression(self, ctx:TSqlParser.Query_expressionContext):
        pass


    # Enter a parse tree produced by TSqlParser#sql_union.
    def enterSql_union(self, ctx:TSqlParser.Sql_unionContext):
        pass

    # Exit a parse tree produced by TSqlParser#sql_union.
    def exitSql_union(self, ctx:TSqlParser.Sql_unionContext):
        pass


    # Enter a parse tree produced by TSqlParser#query_specification.
    def enterQuery_specification(self, ctx:TSqlParser.Query_specificationContext):
        pass

    # Exit a parse tree produced by TSqlParser#query_specification.
    def exitQuery_specification(self, ctx:TSqlParser.Query_specificationContext):
        pass


    # Enter a parse tree produced by TSqlParser#top_clause.
    def enterTop_clause(self, ctx:TSqlParser.Top_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#top_clause.
    def exitTop_clause(self, ctx:TSqlParser.Top_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#top_percent.
    def enterTop_percent(self, ctx:TSqlParser.Top_percentContext):
        pass

    # Exit a parse tree produced by TSqlParser#top_percent.
    def exitTop_percent(self, ctx:TSqlParser.Top_percentContext):
        pass


    # Enter a parse tree produced by TSqlParser#top_count.
    def enterTop_count(self, ctx:TSqlParser.Top_countContext):
        pass

    # Exit a parse tree produced by TSqlParser#top_count.
    def exitTop_count(self, ctx:TSqlParser.Top_countContext):
        pass


    # Enter a parse tree produced by TSqlParser#order_by_clause.
    def enterOrder_by_clause(self, ctx:TSqlParser.Order_by_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#order_by_clause.
    def exitOrder_by_clause(self, ctx:TSqlParser.Order_by_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#for_clause.
    def enterFor_clause(self, ctx:TSqlParser.For_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#for_clause.
    def exitFor_clause(self, ctx:TSqlParser.For_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#xml_common_directives.
    def enterXml_common_directives(self, ctx:TSqlParser.Xml_common_directivesContext):
        pass

    # Exit a parse tree produced by TSqlParser#xml_common_directives.
    def exitXml_common_directives(self, ctx:TSqlParser.Xml_common_directivesContext):
        pass


    # Enter a parse tree produced by TSqlParser#order_by_expression.
    def enterOrder_by_expression(self, ctx:TSqlParser.Order_by_expressionContext):
        pass

    # Exit a parse tree produced by TSqlParser#order_by_expression.
    def exitOrder_by_expression(self, ctx:TSqlParser.Order_by_expressionContext):
        pass


    # Enter a parse tree produced by TSqlParser#group_by_item.
    def enterGroup_by_item(self, ctx:TSqlParser.Group_by_itemContext):
        pass

    # Exit a parse tree produced by TSqlParser#group_by_item.
    def exitGroup_by_item(self, ctx:TSqlParser.Group_by_itemContext):
        pass


    # Enter a parse tree produced by TSqlParser#option_clause.
    def enterOption_clause(self, ctx:TSqlParser.Option_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#option_clause.
    def exitOption_clause(self, ctx:TSqlParser.Option_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#option.
    def enterOption(self, ctx:TSqlParser.OptionContext):
        pass

    # Exit a parse tree produced by TSqlParser#option.
    def exitOption(self, ctx:TSqlParser.OptionContext):
        pass


    # Enter a parse tree produced by TSqlParser#optimize_for_arg.
    def enterOptimize_for_arg(self, ctx:TSqlParser.Optimize_for_argContext):
        pass

    # Exit a parse tree produced by TSqlParser#optimize_for_arg.
    def exitOptimize_for_arg(self, ctx:TSqlParser.Optimize_for_argContext):
        pass


    # Enter a parse tree produced by TSqlParser#select_list.
    def enterSelect_list(self, ctx:TSqlParser.Select_listContext):
        pass

    # Exit a parse tree produced by TSqlParser#select_list.
    def exitSelect_list(self, ctx:TSqlParser.Select_listContext):
        pass


    # Enter a parse tree produced by TSqlParser#udt_method_arguments.
    def enterUdt_method_arguments(self, ctx:TSqlParser.Udt_method_argumentsContext):
        pass

    # Exit a parse tree produced by TSqlParser#udt_method_arguments.
    def exitUdt_method_arguments(self, ctx:TSqlParser.Udt_method_argumentsContext):
        pass


    # Enter a parse tree produced by TSqlParser#asterisk.
    def enterAsterisk(self, ctx:TSqlParser.AsteriskContext):
        pass

    # Exit a parse tree produced by TSqlParser#asterisk.
    def exitAsterisk(self, ctx:TSqlParser.AsteriskContext):
        pass


    # Enter a parse tree produced by TSqlParser#column_elem.
    def enterColumn_elem(self, ctx:TSqlParser.Column_elemContext):
        pass

    # Exit a parse tree produced by TSqlParser#column_elem.
    def exitColumn_elem(self, ctx:TSqlParser.Column_elemContext):
        pass


    # Enter a parse tree produced by TSqlParser#udt_elem.
    def enterUdt_elem(self, ctx:TSqlParser.Udt_elemContext):
        pass

    # Exit a parse tree produced by TSqlParser#udt_elem.
    def exitUdt_elem(self, ctx:TSqlParser.Udt_elemContext):
        pass


    # Enter a parse tree produced by TSqlParser#expression_elem.
    def enterExpression_elem(self, ctx:TSqlParser.Expression_elemContext):
        pass

    # Exit a parse tree produced by TSqlParser#expression_elem.
    def exitExpression_elem(self, ctx:TSqlParser.Expression_elemContext):
        pass


    # Enter a parse tree produced by TSqlParser#select_list_elem.
    def enterSelect_list_elem(self, ctx:TSqlParser.Select_list_elemContext):
        pass

    # Exit a parse tree produced by TSqlParser#select_list_elem.
    def exitSelect_list_elem(self, ctx:TSqlParser.Select_list_elemContext):
        pass


    # Enter a parse tree produced by TSqlParser#table_sources.
    def enterTable_sources(self, ctx:TSqlParser.Table_sourcesContext):
        pass

    # Exit a parse tree produced by TSqlParser#table_sources.
    def exitTable_sources(self, ctx:TSqlParser.Table_sourcesContext):
        pass


    # Enter a parse tree produced by TSqlParser#table_source.
    def enterTable_source(self, ctx:TSqlParser.Table_sourceContext):
        pass

    # Exit a parse tree produced by TSqlParser#table_source.
    def exitTable_source(self, ctx:TSqlParser.Table_sourceContext):
        pass


    # Enter a parse tree produced by TSqlParser#table_source_item_joined.
    def enterTable_source_item_joined(self, ctx:TSqlParser.Table_source_item_joinedContext):
        pass

    # Exit a parse tree produced by TSqlParser#table_source_item_joined.
    def exitTable_source_item_joined(self, ctx:TSqlParser.Table_source_item_joinedContext):
        pass


    # Enter a parse tree produced by TSqlParser#table_source_item.
    def enterTable_source_item(self, ctx:TSqlParser.Table_source_itemContext):
        pass

    # Exit a parse tree produced by TSqlParser#table_source_item.
    def exitTable_source_item(self, ctx:TSqlParser.Table_source_itemContext):
        pass


    # Enter a parse tree produced by TSqlParser#open_xml.
    def enterOpen_xml(self, ctx:TSqlParser.Open_xmlContext):
        pass

    # Exit a parse tree produced by TSqlParser#open_xml.
    def exitOpen_xml(self, ctx:TSqlParser.Open_xmlContext):
        pass


    # Enter a parse tree produced by TSqlParser#schema_declaration.
    def enterSchema_declaration(self, ctx:TSqlParser.Schema_declarationContext):
        pass

    # Exit a parse tree produced by TSqlParser#schema_declaration.
    def exitSchema_declaration(self, ctx:TSqlParser.Schema_declarationContext):
        pass


    # Enter a parse tree produced by TSqlParser#column_declaration.
    def enterColumn_declaration(self, ctx:TSqlParser.Column_declarationContext):
        pass

    # Exit a parse tree produced by TSqlParser#column_declaration.
    def exitColumn_declaration(self, ctx:TSqlParser.Column_declarationContext):
        pass


    # Enter a parse tree produced by TSqlParser#change_table.
    def enterChange_table(self, ctx:TSqlParser.Change_tableContext):
        pass

    # Exit a parse tree produced by TSqlParser#change_table.
    def exitChange_table(self, ctx:TSqlParser.Change_tableContext):
        pass


    # Enter a parse tree produced by TSqlParser#join_part.
    def enterJoin_part(self, ctx:TSqlParser.Join_partContext):
        pass

    # Exit a parse tree produced by TSqlParser#join_part.
    def exitJoin_part(self, ctx:TSqlParser.Join_partContext):
        pass


    # Enter a parse tree produced by TSqlParser#pivot_clause.
    def enterPivot_clause(self, ctx:TSqlParser.Pivot_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#pivot_clause.
    def exitPivot_clause(self, ctx:TSqlParser.Pivot_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#unpivot_clause.
    def enterUnpivot_clause(self, ctx:TSqlParser.Unpivot_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#unpivot_clause.
    def exitUnpivot_clause(self, ctx:TSqlParser.Unpivot_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#full_column_name_list.
    def enterFull_column_name_list(self, ctx:TSqlParser.Full_column_name_listContext):
        pass

    # Exit a parse tree produced by TSqlParser#full_column_name_list.
    def exitFull_column_name_list(self, ctx:TSqlParser.Full_column_name_listContext):
        pass


    # Enter a parse tree produced by TSqlParser#table_name_with_hint.
    def enterTable_name_with_hint(self, ctx:TSqlParser.Table_name_with_hintContext):
        pass

    # Exit a parse tree produced by TSqlParser#table_name_with_hint.
    def exitTable_name_with_hint(self, ctx:TSqlParser.Table_name_with_hintContext):
        pass


    # Enter a parse tree produced by TSqlParser#rowset_function.
    def enterRowset_function(self, ctx:TSqlParser.Rowset_functionContext):
        pass

    # Exit a parse tree produced by TSqlParser#rowset_function.
    def exitRowset_function(self, ctx:TSqlParser.Rowset_functionContext):
        pass


    # Enter a parse tree produced by TSqlParser#bulk_option.
    def enterBulk_option(self, ctx:TSqlParser.Bulk_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#bulk_option.
    def exitBulk_option(self, ctx:TSqlParser.Bulk_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#derived_table.
    def enterDerived_table(self, ctx:TSqlParser.Derived_tableContext):
        pass

    # Exit a parse tree produced by TSqlParser#derived_table.
    def exitDerived_table(self, ctx:TSqlParser.Derived_tableContext):
        pass


    # Enter a parse tree produced by TSqlParser#RANKING_WINDOWED_FUNC.
    def enterRANKING_WINDOWED_FUNC(self, ctx:TSqlParser.RANKING_WINDOWED_FUNCContext):
        pass

    # Exit a parse tree produced by TSqlParser#RANKING_WINDOWED_FUNC.
    def exitRANKING_WINDOWED_FUNC(self, ctx:TSqlParser.RANKING_WINDOWED_FUNCContext):
        pass


    # Enter a parse tree produced by TSqlParser#AGGREGATE_WINDOWED_FUNC.
    def enterAGGREGATE_WINDOWED_FUNC(self, ctx:TSqlParser.AGGREGATE_WINDOWED_FUNCContext):
        pass

    # Exit a parse tree produced by TSqlParser#AGGREGATE_WINDOWED_FUNC.
    def exitAGGREGATE_WINDOWED_FUNC(self, ctx:TSqlParser.AGGREGATE_WINDOWED_FUNCContext):
        pass


    # Enter a parse tree produced by TSqlParser#ANALYTIC_WINDOWED_FUNC.
    def enterANALYTIC_WINDOWED_FUNC(self, ctx:TSqlParser.ANALYTIC_WINDOWED_FUNCContext):
        pass

    # Exit a parse tree produced by TSqlParser#ANALYTIC_WINDOWED_FUNC.
    def exitANALYTIC_WINDOWED_FUNC(self, ctx:TSqlParser.ANALYTIC_WINDOWED_FUNCContext):
        pass


    # Enter a parse tree produced by TSqlParser#SCALAR_FUNCTION.
    def enterSCALAR_FUNCTION(self, ctx:TSqlParser.SCALAR_FUNCTIONContext):
        pass

    # Exit a parse tree produced by TSqlParser#SCALAR_FUNCTION.
    def exitSCALAR_FUNCTION(self, ctx:TSqlParser.SCALAR_FUNCTIONContext):
        pass


    # Enter a parse tree produced by TSqlParser#BINARY_CHECKSUM.
    def enterBINARY_CHECKSUM(self, ctx:TSqlParser.BINARY_CHECKSUMContext):
        pass

    # Exit a parse tree produced by TSqlParser#BINARY_CHECKSUM.
    def exitBINARY_CHECKSUM(self, ctx:TSqlParser.BINARY_CHECKSUMContext):
        pass


    # Enter a parse tree produced by TSqlParser#CAST.
    def enterCAST(self, ctx:TSqlParser.CASTContext):
        pass

    # Exit a parse tree produced by TSqlParser#CAST.
    def exitCAST(self, ctx:TSqlParser.CASTContext):
        pass


    # Enter a parse tree produced by TSqlParser#CONVERT.
    def enterCONVERT(self, ctx:TSqlParser.CONVERTContext):
        pass

    # Exit a parse tree produced by TSqlParser#CONVERT.
    def exitCONVERT(self, ctx:TSqlParser.CONVERTContext):
        pass


    # Enter a parse tree produced by TSqlParser#CHECKSUM.
    def enterCHECKSUM(self, ctx:TSqlParser.CHECKSUMContext):
        pass

    # Exit a parse tree produced by TSqlParser#CHECKSUM.
    def exitCHECKSUM(self, ctx:TSqlParser.CHECKSUMContext):
        pass


    # Enter a parse tree produced by TSqlParser#COALESCE.
    def enterCOALESCE(self, ctx:TSqlParser.COALESCEContext):
        pass

    # Exit a parse tree produced by TSqlParser#COALESCE.
    def exitCOALESCE(self, ctx:TSqlParser.COALESCEContext):
        pass


    # Enter a parse tree produced by TSqlParser#CURRENT_TIMESTAMP.
    def enterCURRENT_TIMESTAMP(self, ctx:TSqlParser.CURRENT_TIMESTAMPContext):
        pass

    # Exit a parse tree produced by TSqlParser#CURRENT_TIMESTAMP.
    def exitCURRENT_TIMESTAMP(self, ctx:TSqlParser.CURRENT_TIMESTAMPContext):
        pass


    # Enter a parse tree produced by TSqlParser#CURRENT_USER.
    def enterCURRENT_USER(self, ctx:TSqlParser.CURRENT_USERContext):
        pass

    # Exit a parse tree produced by TSqlParser#CURRENT_USER.
    def exitCURRENT_USER(self, ctx:TSqlParser.CURRENT_USERContext):
        pass


    # Enter a parse tree produced by TSqlParser#DATEADD.
    def enterDATEADD(self, ctx:TSqlParser.DATEADDContext):
        pass

    # Exit a parse tree produced by TSqlParser#DATEADD.
    def exitDATEADD(self, ctx:TSqlParser.DATEADDContext):
        pass


    # Enter a parse tree produced by TSqlParser#DATEDIFF.
    def enterDATEDIFF(self, ctx:TSqlParser.DATEDIFFContext):
        pass

    # Exit a parse tree produced by TSqlParser#DATEDIFF.
    def exitDATEDIFF(self, ctx:TSqlParser.DATEDIFFContext):
        pass


    # Enter a parse tree produced by TSqlParser#DATENAME.
    def enterDATENAME(self, ctx:TSqlParser.DATENAMEContext):
        pass

    # Exit a parse tree produced by TSqlParser#DATENAME.
    def exitDATENAME(self, ctx:TSqlParser.DATENAMEContext):
        pass


    # Enter a parse tree produced by TSqlParser#DATEPART.
    def enterDATEPART(self, ctx:TSqlParser.DATEPARTContext):
        pass

    # Exit a parse tree produced by TSqlParser#DATEPART.
    def exitDATEPART(self, ctx:TSqlParser.DATEPARTContext):
        pass


    # Enter a parse tree produced by TSqlParser#GETDATE.
    def enterGETDATE(self, ctx:TSqlParser.GETDATEContext):
        pass

    # Exit a parse tree produced by TSqlParser#GETDATE.
    def exitGETDATE(self, ctx:TSqlParser.GETDATEContext):
        pass


    # Enter a parse tree produced by TSqlParser#GETUTCDATE.
    def enterGETUTCDATE(self, ctx:TSqlParser.GETUTCDATEContext):
        pass

    # Exit a parse tree produced by TSqlParser#GETUTCDATE.
    def exitGETUTCDATE(self, ctx:TSqlParser.GETUTCDATEContext):
        pass


    # Enter a parse tree produced by TSqlParser#IDENTITY.
    def enterIDENTITY(self, ctx:TSqlParser.IDENTITYContext):
        pass

    # Exit a parse tree produced by TSqlParser#IDENTITY.
    def exitIDENTITY(self, ctx:TSqlParser.IDENTITYContext):
        pass


    # Enter a parse tree produced by TSqlParser#MIN_ACTIVE_ROWVERSION.
    def enterMIN_ACTIVE_ROWVERSION(self, ctx:TSqlParser.MIN_ACTIVE_ROWVERSIONContext):
        pass

    # Exit a parse tree produced by TSqlParser#MIN_ACTIVE_ROWVERSION.
    def exitMIN_ACTIVE_ROWVERSION(self, ctx:TSqlParser.MIN_ACTIVE_ROWVERSIONContext):
        pass


    # Enter a parse tree produced by TSqlParser#NULLIF.
    def enterNULLIF(self, ctx:TSqlParser.NULLIFContext):
        pass

    # Exit a parse tree produced by TSqlParser#NULLIF.
    def exitNULLIF(self, ctx:TSqlParser.NULLIFContext):
        pass


    # Enter a parse tree produced by TSqlParser#STUFF.
    def enterSTUFF(self, ctx:TSqlParser.STUFFContext):
        pass

    # Exit a parse tree produced by TSqlParser#STUFF.
    def exitSTUFF(self, ctx:TSqlParser.STUFFContext):
        pass


    # Enter a parse tree produced by TSqlParser#SESSION_USER.
    def enterSESSION_USER(self, ctx:TSqlParser.SESSION_USERContext):
        pass

    # Exit a parse tree produced by TSqlParser#SESSION_USER.
    def exitSESSION_USER(self, ctx:TSqlParser.SESSION_USERContext):
        pass


    # Enter a parse tree produced by TSqlParser#SYSTEM_USER.
    def enterSYSTEM_USER(self, ctx:TSqlParser.SYSTEM_USERContext):
        pass

    # Exit a parse tree produced by TSqlParser#SYSTEM_USER.
    def exitSYSTEM_USER(self, ctx:TSqlParser.SYSTEM_USERContext):
        pass


    # Enter a parse tree produced by TSqlParser#ISNULL.
    def enterISNULL(self, ctx:TSqlParser.ISNULLContext):
        pass

    # Exit a parse tree produced by TSqlParser#ISNULL.
    def exitISNULL(self, ctx:TSqlParser.ISNULLContext):
        pass


    # Enter a parse tree produced by TSqlParser#XML_DATA_TYPE_FUNC.
    def enterXML_DATA_TYPE_FUNC(self, ctx:TSqlParser.XML_DATA_TYPE_FUNCContext):
        pass

    # Exit a parse tree produced by TSqlParser#XML_DATA_TYPE_FUNC.
    def exitXML_DATA_TYPE_FUNC(self, ctx:TSqlParser.XML_DATA_TYPE_FUNCContext):
        pass


    # Enter a parse tree produced by TSqlParser#xml_data_type_methods.
    def enterXml_data_type_methods(self, ctx:TSqlParser.Xml_data_type_methodsContext):
        pass

    # Exit a parse tree produced by TSqlParser#xml_data_type_methods.
    def exitXml_data_type_methods(self, ctx:TSqlParser.Xml_data_type_methodsContext):
        pass


    # Enter a parse tree produced by TSqlParser#value_method.
    def enterValue_method(self, ctx:TSqlParser.Value_methodContext):
        pass

    # Exit a parse tree produced by TSqlParser#value_method.
    def exitValue_method(self, ctx:TSqlParser.Value_methodContext):
        pass


    # Enter a parse tree produced by TSqlParser#query_method.
    def enterQuery_method(self, ctx:TSqlParser.Query_methodContext):
        pass

    # Exit a parse tree produced by TSqlParser#query_method.
    def exitQuery_method(self, ctx:TSqlParser.Query_methodContext):
        pass


    # Enter a parse tree produced by TSqlParser#exist_method.
    def enterExist_method(self, ctx:TSqlParser.Exist_methodContext):
        pass

    # Exit a parse tree produced by TSqlParser#exist_method.
    def exitExist_method(self, ctx:TSqlParser.Exist_methodContext):
        pass


    # Enter a parse tree produced by TSqlParser#modify_method.
    def enterModify_method(self, ctx:TSqlParser.Modify_methodContext):
        pass

    # Exit a parse tree produced by TSqlParser#modify_method.
    def exitModify_method(self, ctx:TSqlParser.Modify_methodContext):
        pass


    # Enter a parse tree produced by TSqlParser#nodes_method.
    def enterNodes_method(self, ctx:TSqlParser.Nodes_methodContext):
        pass

    # Exit a parse tree produced by TSqlParser#nodes_method.
    def exitNodes_method(self, ctx:TSqlParser.Nodes_methodContext):
        pass


    # Enter a parse tree produced by TSqlParser#switch_section.
    def enterSwitch_section(self, ctx:TSqlParser.Switch_sectionContext):
        pass

    # Exit a parse tree produced by TSqlParser#switch_section.
    def exitSwitch_section(self, ctx:TSqlParser.Switch_sectionContext):
        pass


    # Enter a parse tree produced by TSqlParser#switch_search_condition_section.
    def enterSwitch_search_condition_section(self, ctx:TSqlParser.Switch_search_condition_sectionContext):
        pass

    # Exit a parse tree produced by TSqlParser#switch_search_condition_section.
    def exitSwitch_search_condition_section(self, ctx:TSqlParser.Switch_search_condition_sectionContext):
        pass


    # Enter a parse tree produced by TSqlParser#as_column_alias.
    def enterAs_column_alias(self, ctx:TSqlParser.As_column_aliasContext):
        pass

    # Exit a parse tree produced by TSqlParser#as_column_alias.
    def exitAs_column_alias(self, ctx:TSqlParser.As_column_aliasContext):
        pass


    # Enter a parse tree produced by TSqlParser#as_table_alias.
    def enterAs_table_alias(self, ctx:TSqlParser.As_table_aliasContext):
        pass

    # Exit a parse tree produced by TSqlParser#as_table_alias.
    def exitAs_table_alias(self, ctx:TSqlParser.As_table_aliasContext):
        pass


    # Enter a parse tree produced by TSqlParser#table_alias.
    def enterTable_alias(self, ctx:TSqlParser.Table_aliasContext):
        pass

    # Exit a parse tree produced by TSqlParser#table_alias.
    def exitTable_alias(self, ctx:TSqlParser.Table_aliasContext):
        pass


    # Enter a parse tree produced by TSqlParser#with_table_hints.
    def enterWith_table_hints(self, ctx:TSqlParser.With_table_hintsContext):
        pass

    # Exit a parse tree produced by TSqlParser#with_table_hints.
    def exitWith_table_hints(self, ctx:TSqlParser.With_table_hintsContext):
        pass


    # Enter a parse tree produced by TSqlParser#insert_with_table_hints.
    def enterInsert_with_table_hints(self, ctx:TSqlParser.Insert_with_table_hintsContext):
        pass

    # Exit a parse tree produced by TSqlParser#insert_with_table_hints.
    def exitInsert_with_table_hints(self, ctx:TSqlParser.Insert_with_table_hintsContext):
        pass


    # Enter a parse tree produced by TSqlParser#table_hint.
    def enterTable_hint(self, ctx:TSqlParser.Table_hintContext):
        pass

    # Exit a parse tree produced by TSqlParser#table_hint.
    def exitTable_hint(self, ctx:TSqlParser.Table_hintContext):
        pass


    # Enter a parse tree produced by TSqlParser#index_value.
    def enterIndex_value(self, ctx:TSqlParser.Index_valueContext):
        pass

    # Exit a parse tree produced by TSqlParser#index_value.
    def exitIndex_value(self, ctx:TSqlParser.Index_valueContext):
        pass


    # Enter a parse tree produced by TSqlParser#column_alias_list.
    def enterColumn_alias_list(self, ctx:TSqlParser.Column_alias_listContext):
        pass

    # Exit a parse tree produced by TSqlParser#column_alias_list.
    def exitColumn_alias_list(self, ctx:TSqlParser.Column_alias_listContext):
        pass


    # Enter a parse tree produced by TSqlParser#column_alias.
    def enterColumn_alias(self, ctx:TSqlParser.Column_aliasContext):
        pass

    # Exit a parse tree produced by TSqlParser#column_alias.
    def exitColumn_alias(self, ctx:TSqlParser.Column_aliasContext):
        pass


    # Enter a parse tree produced by TSqlParser#table_value_constructor.
    def enterTable_value_constructor(self, ctx:TSqlParser.Table_value_constructorContext):
        pass

    # Exit a parse tree produced by TSqlParser#table_value_constructor.
    def exitTable_value_constructor(self, ctx:TSqlParser.Table_value_constructorContext):
        pass


    # Enter a parse tree produced by TSqlParser#expression_list.
    def enterExpression_list(self, ctx:TSqlParser.Expression_listContext):
        pass

    # Exit a parse tree produced by TSqlParser#expression_list.
    def exitExpression_list(self, ctx:TSqlParser.Expression_listContext):
        pass


    # Enter a parse tree produced by TSqlParser#ranking_windowed_function.
    def enterRanking_windowed_function(self, ctx:TSqlParser.Ranking_windowed_functionContext):
        pass

    # Exit a parse tree produced by TSqlParser#ranking_windowed_function.
    def exitRanking_windowed_function(self, ctx:TSqlParser.Ranking_windowed_functionContext):
        pass


    # Enter a parse tree produced by TSqlParser#aggregate_windowed_function.
    def enterAggregate_windowed_function(self, ctx:TSqlParser.Aggregate_windowed_functionContext):
        pass

    # Exit a parse tree produced by TSqlParser#aggregate_windowed_function.
    def exitAggregate_windowed_function(self, ctx:TSqlParser.Aggregate_windowed_functionContext):
        pass


    # Enter a parse tree produced by TSqlParser#analytic_windowed_function.
    def enterAnalytic_windowed_function(self, ctx:TSqlParser.Analytic_windowed_functionContext):
        pass

    # Exit a parse tree produced by TSqlParser#analytic_windowed_function.
    def exitAnalytic_windowed_function(self, ctx:TSqlParser.Analytic_windowed_functionContext):
        pass


    # Enter a parse tree produced by TSqlParser#all_distinct_expression.
    def enterAll_distinct_expression(self, ctx:TSqlParser.All_distinct_expressionContext):
        pass

    # Exit a parse tree produced by TSqlParser#all_distinct_expression.
    def exitAll_distinct_expression(self, ctx:TSqlParser.All_distinct_expressionContext):
        pass


    # Enter a parse tree produced by TSqlParser#over_clause.
    def enterOver_clause(self, ctx:TSqlParser.Over_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#over_clause.
    def exitOver_clause(self, ctx:TSqlParser.Over_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#row_or_range_clause.
    def enterRow_or_range_clause(self, ctx:TSqlParser.Row_or_range_clauseContext):
        pass

    # Exit a parse tree produced by TSqlParser#row_or_range_clause.
    def exitRow_or_range_clause(self, ctx:TSqlParser.Row_or_range_clauseContext):
        pass


    # Enter a parse tree produced by TSqlParser#window_frame_extent.
    def enterWindow_frame_extent(self, ctx:TSqlParser.Window_frame_extentContext):
        pass

    # Exit a parse tree produced by TSqlParser#window_frame_extent.
    def exitWindow_frame_extent(self, ctx:TSqlParser.Window_frame_extentContext):
        pass


    # Enter a parse tree produced by TSqlParser#window_frame_bound.
    def enterWindow_frame_bound(self, ctx:TSqlParser.Window_frame_boundContext):
        pass

    # Exit a parse tree produced by TSqlParser#window_frame_bound.
    def exitWindow_frame_bound(self, ctx:TSqlParser.Window_frame_boundContext):
        pass


    # Enter a parse tree produced by TSqlParser#window_frame_preceding.
    def enterWindow_frame_preceding(self, ctx:TSqlParser.Window_frame_precedingContext):
        pass

    # Exit a parse tree produced by TSqlParser#window_frame_preceding.
    def exitWindow_frame_preceding(self, ctx:TSqlParser.Window_frame_precedingContext):
        pass


    # Enter a parse tree produced by TSqlParser#window_frame_following.
    def enterWindow_frame_following(self, ctx:TSqlParser.Window_frame_followingContext):
        pass

    # Exit a parse tree produced by TSqlParser#window_frame_following.
    def exitWindow_frame_following(self, ctx:TSqlParser.Window_frame_followingContext):
        pass


    # Enter a parse tree produced by TSqlParser#create_database_option.
    def enterCreate_database_option(self, ctx:TSqlParser.Create_database_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#create_database_option.
    def exitCreate_database_option(self, ctx:TSqlParser.Create_database_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#database_filestream_option.
    def enterDatabase_filestream_option(self, ctx:TSqlParser.Database_filestream_optionContext):
        pass

    # Exit a parse tree produced by TSqlParser#database_filestream_option.
    def exitDatabase_filestream_option(self, ctx:TSqlParser.Database_filestream_optionContext):
        pass


    # Enter a parse tree produced by TSqlParser#database_file_spec.
    def enterDatabase_file_spec(self, ctx:TSqlParser.Database_file_specContext):
        pass

    # Exit a parse tree produced by TSqlParser#database_file_spec.
    def exitDatabase_file_spec(self, ctx:TSqlParser.Database_file_specContext):
        pass


    # Enter a parse tree produced by TSqlParser#file_group.
    def enterFile_group(self, ctx:TSqlParser.File_groupContext):
        pass

    # Exit a parse tree produced by TSqlParser#file_group.
    def exitFile_group(self, ctx:TSqlParser.File_groupContext):
        pass


    # Enter a parse tree produced by TSqlParser#file_spec.
    def enterFile_spec(self, ctx:TSqlParser.File_specContext):
        pass

    # Exit a parse tree produced by TSqlParser#file_spec.
    def exitFile_spec(self, ctx:TSqlParser.File_specContext):
        pass


    # Enter a parse tree produced by TSqlParser#entity_name.
    def enterEntity_name(self, ctx:TSqlParser.Entity_nameContext):
        pass

    # Exit a parse tree produced by TSqlParser#entity_name.
    def exitEntity_name(self, ctx:TSqlParser.Entity_nameContext):
        pass


    # Enter a parse tree produced by TSqlParser#entity_name_for_azure_dw.
    def enterEntity_name_for_azure_dw(self, ctx:TSqlParser.Entity_name_for_azure_dwContext):
        pass

    # Exit a parse tree produced by TSqlParser#entity_name_for_azure_dw.
    def exitEntity_name_for_azure_dw(self, ctx:TSqlParser.Entity_name_for_azure_dwContext):
        pass


    # Enter a parse tree produced by TSqlParser#entity_name_for_parallel_dw.
    def enterEntity_name_for_parallel_dw(self, ctx:TSqlParser.Entity_name_for_parallel_dwContext):
        pass

    # Exit a parse tree produced by TSqlParser#entity_name_for_parallel_dw.
    def exitEntity_name_for_parallel_dw(self, ctx:TSqlParser.Entity_name_for_parallel_dwContext):
        pass


    # Enter a parse tree produced by TSqlParser#full_table_name.
    def enterFull_table_name(self, ctx:TSqlParser.Full_table_nameContext):
        pass

    # Exit a parse tree produced by TSqlParser#full_table_name.
    def exitFull_table_name(self, ctx:TSqlParser.Full_table_nameContext):
        pass


    # Enter a parse tree produced by TSqlParser#table_name.
    def enterTable_name(self, ctx:TSqlParser.Table_nameContext):
        pass

    # Exit a parse tree produced by TSqlParser#table_name.
    def exitTable_name(self, ctx:TSqlParser.Table_nameContext):
        pass


    # Enter a parse tree produced by TSqlParser#simple_name.
    def enterSimple_name(self, ctx:TSqlParser.Simple_nameContext):
        pass

    # Exit a parse tree produced by TSqlParser#simple_name.
    def exitSimple_name(self, ctx:TSqlParser.Simple_nameContext):
        pass


    # Enter a parse tree produced by TSqlParser#func_proc_name.
    def enterFunc_proc_name(self, ctx:TSqlParser.Func_proc_nameContext):
        pass

    # Exit a parse tree produced by TSqlParser#func_proc_name.
    def exitFunc_proc_name(self, ctx:TSqlParser.Func_proc_nameContext):
        pass


    # Enter a parse tree produced by TSqlParser#ddl_object.
    def enterDdl_object(self, ctx:TSqlParser.Ddl_objectContext):
        pass

    # Exit a parse tree produced by TSqlParser#ddl_object.
    def exitDdl_object(self, ctx:TSqlParser.Ddl_objectContext):
        pass


    # Enter a parse tree produced by TSqlParser#full_column_name.
    def enterFull_column_name(self, ctx:TSqlParser.Full_column_nameContext):
        pass

    # Exit a parse tree produced by TSqlParser#full_column_name.
    def exitFull_column_name(self, ctx:TSqlParser.Full_column_nameContext):
        pass


    # Enter a parse tree produced by TSqlParser#column_name_list_with_order.
    def enterColumn_name_list_with_order(self, ctx:TSqlParser.Column_name_list_with_orderContext):
        pass

    # Exit a parse tree produced by TSqlParser#column_name_list_with_order.
    def exitColumn_name_list_with_order(self, ctx:TSqlParser.Column_name_list_with_orderContext):
        pass


    # Enter a parse tree produced by TSqlParser#column_name_list.
    def enterColumn_name_list(self, ctx:TSqlParser.Column_name_listContext):
        pass

    # Exit a parse tree produced by TSqlParser#column_name_list.
    def exitColumn_name_list(self, ctx:TSqlParser.Column_name_listContext):
        pass


    # Enter a parse tree produced by TSqlParser#cursor_name.
    def enterCursor_name(self, ctx:TSqlParser.Cursor_nameContext):
        pass

    # Exit a parse tree produced by TSqlParser#cursor_name.
    def exitCursor_name(self, ctx:TSqlParser.Cursor_nameContext):
        pass


    # Enter a parse tree produced by TSqlParser#on_off.
    def enterOn_off(self, ctx:TSqlParser.On_offContext):
        pass

    # Exit a parse tree produced by TSqlParser#on_off.
    def exitOn_off(self, ctx:TSqlParser.On_offContext):
        pass


    # Enter a parse tree produced by TSqlParser#clustered.
    def enterClustered(self, ctx:TSqlParser.ClusteredContext):
        pass

    # Exit a parse tree produced by TSqlParser#clustered.
    def exitClustered(self, ctx:TSqlParser.ClusteredContext):
        pass


    # Enter a parse tree produced by TSqlParser#null_notnull.
    def enterNull_notnull(self, ctx:TSqlParser.Null_notnullContext):
        pass

    # Exit a parse tree produced by TSqlParser#null_notnull.
    def exitNull_notnull(self, ctx:TSqlParser.Null_notnullContext):
        pass


    # Enter a parse tree produced by TSqlParser#null_or_default.
    def enterNull_or_default(self, ctx:TSqlParser.Null_or_defaultContext):
        pass

    # Exit a parse tree produced by TSqlParser#null_or_default.
    def exitNull_or_default(self, ctx:TSqlParser.Null_or_defaultContext):
        pass


    # Enter a parse tree produced by TSqlParser#scalar_function_name.
    def enterScalar_function_name(self, ctx:TSqlParser.Scalar_function_nameContext):
        pass

    # Exit a parse tree produced by TSqlParser#scalar_function_name.
    def exitScalar_function_name(self, ctx:TSqlParser.Scalar_function_nameContext):
        pass


    # Enter a parse tree produced by TSqlParser#begin_conversation_timer.
    def enterBegin_conversation_timer(self, ctx:TSqlParser.Begin_conversation_timerContext):
        pass

    # Exit a parse tree produced by TSqlParser#begin_conversation_timer.
    def exitBegin_conversation_timer(self, ctx:TSqlParser.Begin_conversation_timerContext):
        pass


    # Enter a parse tree produced by TSqlParser#begin_conversation_dialog.
    def enterBegin_conversation_dialog(self, ctx:TSqlParser.Begin_conversation_dialogContext):
        pass

    # Exit a parse tree produced by TSqlParser#begin_conversation_dialog.
    def exitBegin_conversation_dialog(self, ctx:TSqlParser.Begin_conversation_dialogContext):
        pass


    # Enter a parse tree produced by TSqlParser#contract_name.
    def enterContract_name(self, ctx:TSqlParser.Contract_nameContext):
        pass

    # Exit a parse tree produced by TSqlParser#contract_name.
    def exitContract_name(self, ctx:TSqlParser.Contract_nameContext):
        pass


    # Enter a parse tree produced by TSqlParser#service_name.
    def enterService_name(self, ctx:TSqlParser.Service_nameContext):
        pass

    # Exit a parse tree produced by TSqlParser#service_name.
    def exitService_name(self, ctx:TSqlParser.Service_nameContext):
        pass


    # Enter a parse tree produced by TSqlParser#end_conversation.
    def enterEnd_conversation(self, ctx:TSqlParser.End_conversationContext):
        pass

    # Exit a parse tree produced by TSqlParser#end_conversation.
    def exitEnd_conversation(self, ctx:TSqlParser.End_conversationContext):
        pass


    # Enter a parse tree produced by TSqlParser#waitfor_conversation.
    def enterWaitfor_conversation(self, ctx:TSqlParser.Waitfor_conversationContext):
        pass

    # Exit a parse tree produced by TSqlParser#waitfor_conversation.
    def exitWaitfor_conversation(self, ctx:TSqlParser.Waitfor_conversationContext):
        pass


    # Enter a parse tree produced by TSqlParser#get_conversation.
    def enterGet_conversation(self, ctx:TSqlParser.Get_conversationContext):
        pass

    # Exit a parse tree produced by TSqlParser#get_conversation.
    def exitGet_conversation(self, ctx:TSqlParser.Get_conversationContext):
        pass


    # Enter a parse tree produced by TSqlParser#queue_id.
    def enterQueue_id(self, ctx:TSqlParser.Queue_idContext):
        pass

    # Exit a parse tree produced by TSqlParser#queue_id.
    def exitQueue_id(self, ctx:TSqlParser.Queue_idContext):
        pass


    # Enter a parse tree produced by TSqlParser#send_conversation.
    def enterSend_conversation(self, ctx:TSqlParser.Send_conversationContext):
        pass

    # Exit a parse tree produced by TSqlParser#send_conversation.
    def exitSend_conversation(self, ctx:TSqlParser.Send_conversationContext):
        pass


    # Enter a parse tree produced by TSqlParser#data_type.
    def enterData_type(self, ctx:TSqlParser.Data_typeContext):
        pass

    # Exit a parse tree produced by TSqlParser#data_type.
    def exitData_type(self, ctx:TSqlParser.Data_typeContext):
        pass


    # Enter a parse tree produced by TSqlParser#default_value.
    def enterDefault_value(self, ctx:TSqlParser.Default_valueContext):
        pass

    # Exit a parse tree produced by TSqlParser#default_value.
    def exitDefault_value(self, ctx:TSqlParser.Default_valueContext):
        pass


    # Enter a parse tree produced by TSqlParser#constant.
    def enterConstant(self, ctx:TSqlParser.ConstantContext):
        pass

    # Exit a parse tree produced by TSqlParser#constant.
    def exitConstant(self, ctx:TSqlParser.ConstantContext):
        pass


    # Enter a parse tree produced by TSqlParser#sign.
    def enterSign(self, ctx:TSqlParser.SignContext):
        pass

    # Exit a parse tree produced by TSqlParser#sign.
    def exitSign(self, ctx:TSqlParser.SignContext):
        pass


    # Enter a parse tree produced by TSqlParser#id.
    def enterId(self, ctx:TSqlParser.IdContext):
        pass

    # Exit a parse tree produced by TSqlParser#id.
    def exitId(self, ctx:TSqlParser.IdContext):
        pass


    # Enter a parse tree produced by TSqlParser#simple_id.
    def enterSimple_id(self, ctx:TSqlParser.Simple_idContext):
        pass

    # Exit a parse tree produced by TSqlParser#simple_id.
    def exitSimple_id(self, ctx:TSqlParser.Simple_idContext):
        pass


    # Enter a parse tree produced by TSqlParser#comparison_operator.
    def enterComparison_operator(self, ctx:TSqlParser.Comparison_operatorContext):
        pass

    # Exit a parse tree produced by TSqlParser#comparison_operator.
    def exitComparison_operator(self, ctx:TSqlParser.Comparison_operatorContext):
        pass


    # Enter a parse tree produced by TSqlParser#assignment_operator.
    def enterAssignment_operator(self, ctx:TSqlParser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by TSqlParser#assignment_operator.
    def exitAssignment_operator(self, ctx:TSqlParser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by TSqlParser#file_size.
    def enterFile_size(self, ctx:TSqlParser.File_sizeContext):
        pass

    # Exit a parse tree produced by TSqlParser#file_size.
    def exitFile_size(self, ctx:TSqlParser.File_sizeContext):
        pass


