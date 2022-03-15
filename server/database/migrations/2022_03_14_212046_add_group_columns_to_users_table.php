<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class AddGroupColumnsToUsersTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::table('users', function (Blueprint $table) {
            $table->boolean('groups')->default(false);
            $table->unsignedInteger('leader_id')->nullable();
            $table->string('uuid')->nullable();
            $table->boolean('accepting_users')->default(false);
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::table('users', function (Blueprint $table) {
            $table->dropColumn('groups');
            $table->dropColumn('leader_id');
            $table->dropColumn('uuid');
            $table->dropColumn('accepting_users');
        });
    }
}
